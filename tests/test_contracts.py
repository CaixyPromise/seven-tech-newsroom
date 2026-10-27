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
import news_graphics
import image_candidates

def baseline():return json.loads((ROOT/'content/edition.json').read_text())
TEST_DATE=(max(dt.date.fromisoformat(i['date']) for i in baseline()['issues'])+dt.timedelta(days=1)).isoformat()
NOW=TEST_DATE+'T01:00:00+00:00'
LATER=TEST_DATE+'T02:00:00+00:00'
def draft(count=3):
    events=[]
    for n in range(count):
        events.append({'id':f'test-event-{n}','category':'研究','title':f'测试事件 {n}',
          'summary':'仅在测试临时目录使用的摘要','body':['第一段交代测试消息。','第二段提供细节与背景。'],'facts':['一条测试事实'],
          'context':'测试背景','status':'已发布','published_at':TEST_DATE,
          'sources':[{'publisher':'Test','url':f'https://example.com/source-{n}'}],
          'graphic':{'layout':'specs','theme':'blue','eyebrow':'TEST','title':'测试数据图','caption':'测试来源','source_refs':[0],'items':[{'label':'指标一','value':'值一','detail':'事实一'},{'label':'指标二','value':'值二','detail':'事实二'}]}})
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

    def test_new_draft_requires_narrative_body(self):
        d=draft();d['events'][0].pop('body')
        with self.assertRaisesRegex(ValueError,'narrative'):editorial.validate_draft(d)
        d=draft();d['events'][0]['body']='不能把正文写成单个字符串'
        with self.assertRaisesRegex(ValueError,'narrative'):editorial.validate_draft(d)

    def test_prose_is_shared_and_escaped_across_formats(self):
        publisher=build.Publisher('https://example.com/newsroom')
        event=copy.deepcopy(publisher.events['anthropic-s1-ipo-filing'])
        event['body']=['第一段包含 <script> 和 &，需要保留为文字。','第二段是连贯背景。']
        publisher.events[event['id']]=event
        html=publisher.article(event)
        self.assertIn('&lt;script&gt;',html)
        self.assertNotIn('<h2>关键事实</h2>',html)
        self.assertNotIn('<h2>范围与背景</h2>',html)
        issue=next(i for i in publisher.issues if event['id'] in i['event_ids'])
        self.assertIn(event['body'][0],publisher.markdown(issue))
        captured={}
        with patch.object(publisher,'write',side_effect=lambda path,text:captured.update({path:text})):
            publisher.rss()
        import xml.etree.ElementTree as ET
        descriptions=[item.findtext('description') for item in ET.fromstring(captured['feed.xml']).findall('./channel/item')]
        self.assertTrue(any('&lt;script&gt;' in item and event['body'][1] in item for item in descriptions))

    def test_issue_accepts_twenty_but_rejects_twenty_one(self):
        self.assertEqual(editorial.validate_draft(draft(20)),TEST_DATE)
        with self.assertRaisesRegex(ValueError,'3–20'):editorial.validate_draft(draft(21))

    def test_graphics_require_sources_and_safe_local_artwork(self):
        d=draft();d['events'][0]['graphic']['source_refs']=[5]
        with self.assertRaisesRegex(ValueError,'source references'):editorial.validate_draft(d)
        d=draft();d['events'][0]['artwork']={'path':'content/images/../../secrets.png'}
        with self.assertRaisesRegex(ValueError,'local'):editorial.validate_draft(d)
        d=draft();d['events'][0].pop('graphic')
        with self.assertRaisesRegex(ValueError,'graphic brief'):editorial.validate_draft(d)

    def test_graphic_text_is_escaped_and_chart_scale_is_validated(self):
        event=draft()['events'][0];event['issue_date']=TEST_DATE
        event['graphic']['title']='图示 <script> & 内容'
        svg=news_graphics.render(event)
        self.assertIn('&lt;script&gt;',svg)
        self.assertNotIn('<script>',svg)
        event['graphic'].update(layout='bars',axis_max=100)
        for item in event['graphic']['items']:item['amount']=120
        with self.assertRaisesRegex(ValueError,'scale'):news_graphics.render(event)

    def test_image_candidates_are_deduplicated_and_not_approved(self):
        parser=image_candidates.Images('https://example.com/news/')
        parser.feed('<meta property="og:image" content="/hero.jpg"><meta name="twitter:image" content="/hero.jpg"><img src="/logo.png"><img src="javascript:bad"><img src="chart.png" alt="真实图表">')
        self.assertEqual([r['image_url'] for r in parser.rows],['https://example.com/hero.jpg','https://example.com/news/chart.png'])
        with patch.object(image_candidates,'fetch_source',return_value=parser.rows):
            result=image_candidates.discover(draft()['events'][0])
        self.assertTrue(all(r['rights_status']=='needs-review' for r in result['candidates']))
        with patch.object(image_candidates,'fetch_source',side_effect=TimeoutError):
            failed=image_candidates.discover(draft()['events'][0])
        self.assertFalse(failed['candidates'])
        self.assertEqual(failed['errors'][0]['error'],'TimeoutError')

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
            content,issue=editorial.merge(baseline(),draft(20),NOW)
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
