# Seven Tech Newsroom

每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。

[访问网站](https://caixypromise.github.io/seven-tech-newsroom/) · [RSS](https://caixypromise.github.io/seven-tech-newsroom/feed.xml) · [源码仓库](https://github.com/CaixyPromise/seven-tech-newsroom) · [作者主页](https://github.com/CaixyPromise) · [运行说明](OPERATIONS.md)

最近一期：2026-11-09。共 13 期、107 条独立记录；按实际发布状态与来源标时。

**最新数据快照**：2026-11-08 09:08 UTC+8；OpenRouter 日榜另截至 2026-10-31 UTC。

| 观察项 | 最新观测 | 范围 |
| --- | --- | --- |
| 模型基本费估算 | $0.002 · Claude Haiku 5.5 | 7 个选定模型，10K 输入 + 2K 输出 Token |
| 平台单日用量 | 约 7.09T Token · DeepSeek V4.1 Flash 1017 | OpenRouter 2026-10-31 UTC 公开日榜 |
| 开源关注 | 186,286 Stars · ollama/ollama | 本站固定跟踪的 6 个项目 |
| 文本模型下载 | 31,318,908 · openai-community/gpt2 | HF 文本生成类，近 30 日滚动量 |

来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。

## 最新一期 · 2026-11-09

**AI 供电、监管与芯片治理出现新进展**

本期收录 3 条发布窗口内的独立消息：Anthropic 发电设备采购报道、美国 AI 安全评估机构汇报安排变化，以及 Nvidia 董事会启动独立调查。媒体归因、公司表述和未确认事项均在正文中区分。

每日精选，第 013 期。收录范围：2026-11-08 09:00 至 2026-11-09 09:00（Asia/Singapore）。
实际首次整理：2026-11-09 09:10 UTC+8。
指标按实际保存的批次与采集时间查看。

## 1. 报道称 Anthropic 接手 1.7 吉瓦燃气发电机采购承诺

![发电设备采购承诺仍待落地。报道交易额：约 34 亿美元，Financial Times 于 11 月 8 日披露；发电能力：1.7 吉瓦，Reuters 转述的采购承诺规模；供应商：OnePWR Solutions，报道称包含工程与安装能力；履约状态：承诺采购，尚无公开的安装地点或投运日期](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/anthropic-gas-generator-commitments-2026-11-08.svg)

Financial Times 报道的交易数据；Reuters 未能立即独立核实，装机地点与投运时间未披露。

Financial Times 于 11 月 8 日报道称，Anthropic 在 9 月底接手 OnePWR Solutions 的 1.7 吉瓦燃气发电机采购承诺，交易价值约 34 亿美元。Reuters 转述报道说，相关设备由 Caterpillar 供应，交易还包括安装所需的工程与建设能力。

Reuters 表示无法立即独立核实 FT 报道，Anthropic 与 OnePWR 均未回应置评请求；报道也没有披露设备的具体安装地点或投运时间。因此，这笔交易目前是媒体报道的采购承诺，不代表 1.7 吉瓦电力已投入运行。

编辑观察：这笔采购显示数据中心扩张正在争取发电设备供给；实际可提供的电力规模与环境影响，还要看设备何时、何地投入运行。

分类：基础设施；状态：媒体报道；Reuters 未能独立核实，相关公司未回应置评请求；原文日期：2026-11-08。

来源：[Financial Times](https://www.ft.com/content/41bf5c6a-9735-4f1a-a8e3-2bcccad58ba0)
来源：[Reuters](https://www.reuters.com/business/energy/anthropic-secures-34-billion-generator-deal-ai-data-centers-ft-reports-2026-11-08/)

## 2. 美国 AI 安全评估机构人员被要求非正式向白宫汇报

![CAISSI 汇报安排与公开评估现状。机构归属：美国商务部，负责 AI 产品安全评估的独立部门；人员汇报：非正式向白宫汇报，消息来自两名了解讨论的前官员；公开研究：已停止发布，美联社报道的当前状态；年度经费：1,000 万美元，美联社报道](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/us-caissi-informal-white-house-reporting-2026-11-08.svg)

美联社根据两名前政府官员的说法报道；人员汇报安排被描述为非正式。

美联社 11 月 8 日报道，美国商务部下属、负责评估 AI 产品安全的 CAISSI 工作人员，近期被要求非正式向白宫办公室汇报；消息来自两名了解相关讨论的前政府官员。该中心目前没有常任负责人，也已停止公开发布部分 AI 系统安全评估研究。

报道说，中心年度经费为 1,000 万美元。白宫没有回应有关 CAISSI 的具体问题，只表示总统已正式设立“超级智能”工作组，并委托顾问委员会提交 AI 风险报告。美联社称相关汇报安排是非正式的，目前未见正式组织调整文件。

编辑观察：报道揭示的是汇报安排和公开研究现状；后续评估工作是否恢复公开，将是观察该机构独立审查职能变化的直接线索。

分类：治理；状态：美联社报道；汇报安排为匿名消息人士所述的非正式安排；原文日期：2026-11-08。

来源：[Associated Press](https://apnews.com/article/ai-safety-trump-white-house-d3318eb2cf011df53e9ddb3e03d25f13)

## 3. Nvidia 董事会就黄仁勋相关报道启动独立调查

![董事会回应相关报道并启动调查。媒体报道：黄仁勋遭外国情报活动针对，作为董事会调查的报道背景；公司行动：启动独立调查，Nvidia 董事会 11 月 8 日表态；董事会说法：目前无理由认为机密泄露，Reuters 转述的公司立场；待公布：范围与完成时间，截至报道发布尚未披露](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/nvidia-board-foreign-intelligence-review-2026-11-08.svg)

Nvidia 董事会说法由 Reuters 转述；调查范围与时间表尚未公布。

Nvidia 董事会 11 月 8 日表示，将对有关创办人兼 CEO 黄仁勋成为外国情报活动目标的报道启动独立调查。Reuters 报道称，董事会称目前没有理由相信美国国家安全或 Nvidia 公司机密已遭泄露。

这项调查是公司回应相关媒体报道后的行动；截至 Reuters 发布消息，Nvidia 尚未公布调查范围、负责人或完成时间。有关情报活动的说法仍属于媒体报道背景，公开信息尚未证明公司资料已泄露或供应链受到影响。

编辑观察：后续公布的调查范围与证据，将决定外界能否判断这项审查是否解答了围绕芯片出口和供应链安全的疑问。

分类：治理；状态：Nvidia 董事会表态经 Reuters 报道；相关背景指称尚非已证实结论；原文日期：2026-11-08。

来源：[Reuters](https://www.investing.com/news/stock-market-news/nvidia-launches-probe-after-report-ceo-huang-was-target-of-foreign-intelligence-5010307)
来源：[Associated Press](https://apnews.com/article/68839e7ca6ba2b121529f7e475e501d6)

**历史归档**

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
