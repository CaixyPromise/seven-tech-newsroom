# Seven Tech Newsroom

每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。

[访问网站](https://caixypromise.github.io/seven-tech-newsroom/) · [RSS](https://caixypromise.github.io/seven-tech-newsroom/feed.xml) · [源码仓库](https://github.com/CaixyPromise/seven-tech-newsroom) · [作者主页](https://github.com/CaixyPromise) · [运行说明](OPERATIONS.md)

最近一期：2026-11-16。共 19 期、160 条独立记录；按实际发布状态与来源标时。

**最新数据快照**：2026-11-14 09:04 UTC+8；OpenRouter 日榜另截至 2026-10-31 UTC。

| 观察项 | 最新观测 | 范围 |
| --- | --- | --- |
| 模型基本费估算 | $0.00138 · DeepSeek V4.1 Flash 1017 | 7 个选定模型，10K 输入 + 2K 输出 Token |
| 平台单日用量 | 约 7.09T Token · DeepSeek V4.1 Flash 1017 | OpenRouter 2026-10-31 UTC 公开日榜 |
| 开源关注 | 186,899 Stars · ollama/ollama | 本站固定跟踪的 6 个项目 |
| 文本模型下载 | 33,264,897 · openai-community/gpt2 | HF 文本生成类，近 30 日滚动量 |

来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。

## 最新一期 · 2026-11-16

**平台治理、云服务恢复与芯片出口审查**

Meta 在意大利因图库权限被罚，Microsoft 365 报告服务恢复；美国对 AI 芯片出口的审查也在升温。

每日精选，第 019 期。收录范围：2026-11-14 09:00 至 2026-11-16 09:00（Asia/Singapore，UTC+8；承接 11 月 15 日未达最低条数的窗口）。
实际首次整理：2026-11-16 09:10 UTC+8。
指标按实际保存的批次与采集时间查看。

## 1. 意大利对 Meta 处以 8.05 亿欧元罚款，要求图库权限单独征求同意

![图库访问须有独立同意。罚款：€805 million，针对 Facebook Android 图库建议功能；监管机构估计：约 2,000 万人，意大利 Android 用户；60 天内：默认关闭，以单独、明确授权后再启用；调查范围：不含 AI 训练，Meta 否认将图库内容用于训练](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/meta-italy-gallery-permission-fine-2026-11-14.svg)

罚款与整改要求据意大利数据保护机构公告；约 2000 万用户为监管机构估计。

意大利数据保护机构 11 月 14 日对 Meta Platforms Ireland 处以 8.05 亿欧元罚款，理由是 Facebook Android 应用的图库建议功能在未充分告知用户的情况下访问手机照片、视频及相关元数据。监管机构称，图库访问曾与其他应用功能共用一项权限，相关功能还默认开启；该决定适用意大利隐私法中关于设备信息访问的规定。

Meta 须在 60 天内将这项功能设为默认关闭，并以独立、明确的请求说明用途和关闭方法；若未按期改正，不得在缺少有效同意时启用。监管机构称，案件涉及意大利约 2000 万名 Android 用户。此次调查没有审查内容是否用于训练 AI，Meta 否认将图库内容用于训练。

分类：治理；状态：监管机构已作出处罚决定；整改期限为 60 天；原文日期：2026-11-14。

来源：[Associated Press](https://apnews.com/article/9b3073c52464d5cd0e8facbc57285194)
来源：[Reuters](https://www.investing.com/news/stock-market-news/italy-fines-meta-887-million-over-android-users-data-access-5027329)

更正：2026-11-16T01:11:22+00:00 · 最终复核时补充 Reuters 同日交叉报道，并保留 AP 原始报道。

## 2. Microsoft 称全球 Microsoft 365 故障已完全恢复

![故障状态从逐步恢复转为完全恢复。故障期间：多项服务受影响，包括 Outlook、Teams、SharePoint 与 Copilot；原因说明：网络容量升级，近期网络变更后问题显现；11 月 14 日：宣布完全恢复，剩余受影响地区服务已恢复](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/microsoft-365-full-restoration-2026-11-14.svg)

恢复状态及原因按 Microsoft 11 月 14 日说明；技术复盘尚待发布。

Microsoft 11 月 14 日表示，影响 Outlook、Teams、SharePoint 和 Copilot 等服务的全球性 Microsoft 365 故障已完全恢复。公司称，故障由较早进行的一次网络容量升级引入，随后在近期网络变更后显现；服务团队已完成处理并恢复剩余受影响地区的访问。

这项更新标志着前一日仍处于逐步恢复中的事件进入全面恢复状态。AP 报道指出，故障令多个国家的企业和公共机构无法正常使用邮件及协作服务；Microsoft 表示会继续发布事后复盘，当前披露尚未给出完整技术复盘或总受影响用户数。

分类：基础设施；状态：Microsoft 宣布服务已恢复；事后复盘待发布；原文日期：2026-11-14。

来源：[Microsoft 365 Status](https://status.cloud.microsoft/)
来源：[Associated Press](https://apnews.com/article/microsoft-outage-outlook-email-365-recover-ca395c0f1e51af784b6d70afb6554f6a)

## 3. 美国议员要求审视 AI 芯片出口，Megaspeed 称已启动内部调查

![国会审查与公司回应仍在进行。11 月 14 日：议员要求审视出口限制，围绕先进 AI 芯片对华许可；11 月 15 日：Megaspeed 启动内部调查，针对芯片转运指控；公司回应：相关高管已离职，公司称 Alice Huang 于 2025 年离开](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/nvidia-megaspeed-export-scrutiny-2026-11-14.svg)

日期和各方表态据 AP 报道；所述调查尚未形成违法认定。

英伟达高端芯片流向中国的争议在 11 月 14 日继续引发美国国会关注。美联社报道，两党议员呼吁收紧对先进芯片及 AI 技术的出口限制，并要求政府说明相关出口许可的审查依据；报道将这些讨论置于当时的美中 AI 与经贸议程背景中。

次日，新加坡云服务公司 Megaspeed 表示，受到外界关注的 Alice Huang 已于 2025 年 8 月离开公司，目前没有职务，并称已对芯片是否被转运至中国的指控启动内部调查。AP 同时报道新加坡方面曾就服务器采购申报启动调查。上述说法均属公司回应及调查信息，不能据此认定出口违规已被证实。

分类：产业；状态：出口管制审查与公司内部调查进行中；指控未形成定论；原文日期：2026-11-15。

来源：[Associated Press](https://apnews.com/article/aba7f92a1ec2f0f9e4b4da206d640d61)
来源：[Associated Press](https://apnews.com/article/singapore-megaspeed-alice-huang-nvidia-probe-e9e2e18169dce0b30a34f39715bf35ed)

**历史归档**

- [2026-11-16 · 平台治理、云服务恢复与芯片出口审查](archive/2026-11-16.md)
- [2026-11-14 · AI 数据、代理支付与基础设施的新进展](archive/2026-11-14.md)
- [2026-11-13 · 模型进入产品，AI 基础设施继续扩张](archive/2026-11-13.md)
- [2026-11-12 · 本地智能体、机器人模型与多模态决策工具更新](archive/2026-11-12.md)
- [2026-11-11 · 前沿模型、企业智能体与 AI 芯片更新](archive/2026-11-11.md)
- [2026-11-10 · 模型、算力与 AI 工具迎来新一轮更新](archive/2026-11-10.md)
- [2026-11-09 · AI 供电、监管与芯片治理出现新进展](archive/2026-11-09.md)
- [2026-11-08 · 助手工作区、折叠屏应用与 AI 算力项目](archive/2026-11-08.md)
- [2026-11-07 · AI 走进实验室、助手与制造现场](archive/2026-11-07.md)
- [2026-11-06 · AI 安全、机器人与算力建设迎来新进展](archive/2026-11-06.md)
- [2026-11-05 · AI 工具走向工程、研究与企业系统](archive/2026-11-05.md)
- [2026-11-04 · AI 进入工程、教育与企业工作流](archive/2026-11-04.md)
- [2026-11-03 · 模型、算力基础设施与企业 AI 应用继续推进](archive/2026-11-03.md)
- [2026-11-01 · 开放模型、智能体与安全机制迎来新进展](archive/2026-11-01.md)
- [2026-10-29 · 前沿模型、智能体工具与企业部署继续扩展](archive/2026-10-29.md)
- [2026-10-28 · 模型研究、企业代理与 AI 基础设施的多线推进](archive/2026-10-28.md)
- [2026-10-27 · 企业 AI 加入流程与数据层，终端和资本市场出现新动作](archive/2026-10-27.md)
- [2026-10-26 · AI 正在进入工具、数据与日常工作](archive/2026-10-26.md)
- [2026-10-23 · 模型能力向前一步，工具与证据也要跟上](archive/2026-10-23.md)
