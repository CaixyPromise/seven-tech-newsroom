"""Offline regression checks for daily imports, archives and deployed revision checks."""
import copy
import datetime as dt
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import publish_issue as editorial
import build
import check_live
import collect

def baseline():return json.loads((ROOT/'content/edition.json').read_text())
TEST_DATE=(max(dt.date.fromisoformat(i['date']) for i in baseline()['issues'])+dt.timedelta(days=1)).isoformat()
NOW=TEST_DATE+'T01:00:00+00:00'
LATER=TEST_DATE+'T02:00:00+00:00'
def draft():
    events=[]
    for n in range(3):
        events.append({'id':f'test-event-{n}','category':'研究','title':f'测试事件 {n}',
          'summary':'仅在测试临时目录使用的摘要','facts':['一条测试事实'],
          'context':'测试背景','status':'已发布','published_at':TEST_DATE,
          'sources':[{'publisher':'Test','url':f'https://example.com/source-{n}'}]})
    return {'issue':{'date':TEST_DATE,'title':'测试期刊','dek':'离线回归测试',
            'coverage':'仅用于离线测试的下一期','lead_ids':['test-event-0']},'events':events}

class EditorialTests(unittest.TestCase):
    def test_same_day_reimport_preserves_identity_and_sources(self):
        content,issue=editorial.merge(baseline(),draft(),NOW)
        again,second=editorial.merge(content,draft(),LATER)
        self.assertEqual(issue['number'],second['number'])
        self.assertEqual(issue['published_at'],second['published_at'])
        stable=lambda rows:[{k:v for k,v in e.items() if k!='verified_at'} for e in rows]
        self.assertEqual(stable(content['events']),stable(again['events']))
        self.assertEqual(len(content['issues']),len(again['issues']))

    def test_correction_required_and_recorded(self):
        content,_=editorial.merge(baseline(),draft(),NOW)
        changed=draft();changed['events'][0]['summary']='修正后的摘要'
        with self.assertRaisesRegex(ValueError,'correction'):editorial.merge(content,changed,LATER)
        changed['events'][0]['corrections']=[{'at':LATER,'note':'更正测试事实'}]
        result,_=editorial.merge(content,changed,LATER)
        self.assertEqual(result['events'][-3]['summary'],'修正后的摘要')

    def test_duplicate_primary_source_rejected(self):
        d=draft();d['events'][1]['sources']=copy.deepcopy(d['events'][0]['sources'])
        with self.assertRaisesRegex(ValueError,'duplicated'):editorial.validate_draft(d)

    def test_unsafe_id_and_unknown_date_rejected(self):
        d=draft();d['events'][0]['id']='../escape'
        with self.assertRaisesRegex(ValueError,'Unsafe'):editorial.validate_draft(d)
        d=draft();d['events'][0]['published_at']=None
        with self.assertRaisesRegex(ValueError,'labelled'):editorial.validate_draft(d)

    def test_existing_event_cannot_move_to_another_issue(self):
        d=draft();d['events'][0]['id']=baseline()['events'][0]['id'];d['issue']['lead_ids']=[d['events'][0]['id']]
        with self.assertRaisesRegex(ValueError,'different issue'):editorial.merge(baseline(),d,NOW)

    def test_same_day_event_set_is_fixed(self):
        content,_=editorial.merge(baseline(),draft(),NOW)
        d=draft();d['events'][2]['id']='new-event'
        with self.assertRaisesRegex(ValueError,'event set'):editorial.merge(content,d,LATER)

    def test_collection_failure_retains_last_good_snapshot(self):
        previous=(ROOT/'data/snapshot.json').read_bytes()
        failed=[(key,{'error_type':'NetworkFailure'},None) for key in collect.ENDPOINTS]
        with patch.object(collect,'fetch',side_effect=lambda pair:next(x for x in failed if x[0]==pair[0])):
            with self.assertRaisesRegex(SystemExit,'retained'):collect.main()
        self.assertEqual(previous,(ROOT/'data/snapshot.json').read_bytes())

    def test_script_json_cannot_close_script_tag(self):
        encoded=build.script_json({'value':'</script><script>alert(1)</script>'})
        self.assertNotIn('</script>',encoded)
        self.assertEqual(json.loads(encoded)['value'],'</script><script>alert(1)</script>')

    def test_next_issue_build_and_verify(self):
        with tempfile.TemporaryDirectory() as temp:
            repo=Path(temp)/'repo'
            shutil.copytree(ROOT,repo,ignore=shutil.ignore_patterns('.git','dist','output','__pycache__','work','build-manifest.json'))
            content,issue=editorial.merge(baseline(),draft(),NOW)
            (repo/'content/edition.json').write_text(json.dumps(content,ensure_ascii=False))
            frozen={'issue_date':issue['date'],'saved_at':NOW,'snapshot':json.loads((ROOT/'data/snapshot.json').read_text()),'usage':json.loads((ROOT/'data/usage.json').read_text())}
            snapshot_path=repo/issue['metric_snapshot'];snapshot_path.parent.mkdir(parents=True,exist_ok=True);snapshot_path.write_text(json.dumps(frozen))
            for script in ['build.py','verify.py']:
                result=subprocess.run([sys.executable,str(repo/'scripts'/script)],cwd=repo,capture_output=True,text=True)
                self.assertEqual(result.returncode,0,result.stdout+result.stderr)
            self.assertTrue((repo/f'dist/downloads/data/{TEST_DATE}.json').exists())
            self.assertIn('本期数据快照',(repo/f'dist/daily/{TEST_DATE}/index.html').read_text())
            self.assertIn('urn:ai-rizhi:daily:'+TEST_DATE,(repo/'dist/feed.xml').read_text())
            self.assertEqual((ROOT/'content/edition.json').read_text(),json.dumps(baseline(),ensure_ascii=False,indent=2)+'\n')

class LiveCheckTests(unittest.TestCase):
    def test_freshness_mismatch_is_failure(self):
        with patch.object(check_live,'get',return_value=json.dumps({'latest_issue_date':'2026-10-26'})):
            with self.assertRaisesRegex(ValueError,'stale'):check_live.inspect('https://example.com','2026-10-27')

    def test_wrong_commit_is_failure(self):
        with patch.object(check_live,'get',return_value=json.dumps({'latest_issue_date':'2026-10-27','batch_id':'batch','commit_sha':'old'})):
            with self.assertRaisesRegex(ValueError,'commit'):check_live.inspect('https://example.com',expected_commit='new')

if __name__=='__main__':unittest.main()
