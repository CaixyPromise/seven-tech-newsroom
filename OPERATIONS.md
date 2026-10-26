# Seven Tech Newsroom 运行说明

**站点与署名**

- 产品：Seven Tech Newsroom
- 仓库：https://github.com/CaixyPromise/seven-tech-newsroom
- 站点：https://caixypromise.github.io/seven-tech-newsroom/
- 作者及主页：CaixyPromise，https://github.com/CaixyPromise
- 时间：Asia/Singapore，UTC+8

**每日发布链路**

本地 Codex 独立定时任务每天 09:00 开始，由 Agent 搜集、核对和整理新闻，使用本地 GitHub CLI 与 git 推送。推送 main 触发 `Publish GitHub Pages`，完成测试、构建、Pages 部署和远端检查。无需入站服务或回调，所有连接为向外 HTTPS。

本地运行需要 Mac 与 Codex 可用、网络能访问新闻源和 GitHub、`gh auth status` 正常、仓库干净且可快进。平台调度可能延迟，不承诺精确到分钟。源码中没有 API Key；定时整理使用所配置的 Codex 模型，不调用已停用的 GitHub Models。

**开始前**

所有文件和命令都绑定本仓库工作目录。核对：

```sh
git remote get-url origin
git status --short
git branch --show-current
gh auth status
git fetch origin main
git merge --ff-only origin/main
```

远端必须匹配上面的仓库，分支必须为 main。遇到已有无关修改或快进失败，保留现场，不进行 reset、stash 或强推。工作目录外不创建文件。

**新闻搜集与编辑**

1. 读取 `content/edition.json` 和最近两期，避免重复事件。
2. 主动联网搜集上一发布截点至本次截点的 AI/科技动态，官方公告、原始论文与项目发布优先。允许少量迟到消息但标明原文日期；不把旧闻改日期重发。
3. 每个独立事件核实原始来源，中文标题、摘要、1—4 条关键事实、范围说明和状态均须有依据。厂商成绩与独立评测分开。原始发布日期未确认时用 null，并在 status 写“发布日待确认”。
4. 目标 5—10 条，最多 12 条；不足 3 条有效事件则不发布伪日报，保留上一期并报告异常。合并同一事件，多来源可附在同一条。
5. 公开内容不包含内部项目背景、私人资料或本机路径。只保存本站摘要、必要元数据和获准使用的指标，不复制第三方全文或无授权图片。

草稿放在被忽略的 `work/draft-YYYY-MM-DD.json`，格式如下（示例字段，不是可发布新闻）：

```json
{
  "issue": {
    "date": "YYYY-MM-DD",
    "title": "本期总标题",
    "dek": "本期概述",
    "coverage": "实际搜集时间窗口",
    "lead_ids": ["stable-event-id"]
  },
  "events": [{
    "id": "stable-event-id",
    "category": "模型",
    "title": "经核实的中文标题",
    "summary": "有原始来源支持的摘要",
    "facts": ["有依据的关键事实"],
    "context": "限制和背景",
    "status": "已发布",
    "published_at": "YYYY-MM-DD",
    "sources": [{"publisher": "发布者", "url": "https://example.com/original"}]
  }]
}
```

category 可用模型、产品、价格、开源、研究、基础设施、产业、治理。事件 ID 必须稳定，不根据措辞调整随意改名；同一既有事件在另一日有实质进展时采用独立跟进 ID 并在正文关联。

**采集、归档与验证**

```sh
python3 scripts/collect.py
python3 scripts/publish_issue.py --draft work/draft-YYYY-MM-DD.json --check-only
python3 scripts/publish_issue.py --draft work/draft-YYYY-MM-DD.json
python3 -m unittest discover -s tests -v
python3 scripts/build.py
python3 scripts/verify.py
python3 scripts/public_check.py
python3 scripts/public_check.py --dist
```

收集失败须保留上次有效数据和原时间，并说明缺口。OpenRouter 用量在本版本为已核对的公开页面快照；需要更新时使用其日榜及实际截止时间，不假称调用了带 Key 的 API。GitHub Stars 是本站固定跟踪池的总量；HF 是近 30 日滚动下载量。首次无日增，间隔不足一天也不能伪装为日增。

`publish_issue.py` 保留首次发布时间、稳定期号、事件集合及 RSS GUID。同日修正需要追加 corrections 记录；已发布期刊的指标快照保存在 `data/issues/`，不被新指标覆盖。初始两期回溯样刊没有当时快照，明确保留这一事实。

**推送与上线核验**

只 stage 本期内容、数据、归档及 README。逐项核对 diff，禁止 `git add .` 夹带其他文件。使用普通提交和普通 push，不强推。CLI 身份为已授权的 CaixyPromise；凭证保存在本机凭证机制中，不写入仓库或 workflow。

```sh
git add content/edition.json data archive README.md
git diff --cached --stat
git diff --cached
git commit -m "news: publish YYYY-MM-DD edition"
git push origin main
gh run list --workflow publish.yml --branch main --limit 5
```

必须选择刚推送 commit 对应的运行，等待结束并读取结论。成功后：

```sh
python3 scripts/check_live.py --date YYYY-MM-DD --batch EXPECTED_BATCH --commit EXPECTED_COMMIT --retries 6 --delay 10
```

EXPECTED_BATCH 来自本轮 `build-manifest.json`，EXPECTED_COMMIT 为刚推送的完整 SHA。检查会 GET 线上 status、首页、当期页面和 RSS，核对期号、内容批次、commit、Footer 链接和 RSS GUID。失败有限重试；推送、CI、Pages、线上核验分别记录，不能互相代替。

**漏更检查与异常提醒**

GitHub `Daily freshness check` 每天 09:47（UTC+8）独立检查当天线上期号及 RSS。它不写仓库，不生成新闻；漏更会产生失败运行。Actions 自身调度也可能延迟。

Codex 每日任务在发生网络、登录、新闻不足、构建、推送、部署、内容或 RSS 异常时，必须在运行结果中提醒用户并附失败步骤、现有线上版本、是否已推送和恢复建议。GitHub 的失败邮件/应用通知取决于账号通知设置；配置说明见 `https://github.com/settings/notifications`，需要开启 Actions 失败通知。不得把“workflow 已配置”当作通知已经送达的证据。

手动检查或补跑：

```sh
gh workflow run publish.yml
gh workflow run daily-health.yml -f expected_date=YYYY-MM-DD
```

**本地预览**

`python3 preview.py`，或双击 `启动预览.command`。预览器只监听回环地址，页面刷新后读取更新；正式发布使用 `config/site.json` 的公共地址。`dist/`、本地截图与运行清单不提交，CI 从源码重建站点。
