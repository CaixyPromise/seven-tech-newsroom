# Seven Tech Newsroom

每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。

[访问网站](https://caixypromise.github.io/seven-tech-newsroom/) · [RSS](https://caixypromise.github.io/seven-tech-newsroom/feed.xml) · [源码仓库](https://github.com/CaixyPromise/seven-tech-newsroom) · [作者主页](https://github.com/CaixyPromise) · [运行说明](OPERATIONS.md)

最近一期：2026-10-29。共 5 期、40 条独立记录；按实际发布状态与来源标时。

**最新数据快照**：2026-10-29 09:03 UTC+8；OpenRouter 日榜另截至 2026-10-28 UTC。

| 观察项 | 最新观测 | 范围 |
| --- | --- | --- |
| 模型基本费估算 | $0.002 · Claude Haiku 5.5 | 7 个选定模型，10K 输入 + 2K 输出 Token |
| 平台单日用量 | 约 7.3T Token · DeepSeek V4.1 Flash 1017 | OpenRouter 2026-10-28 UTC 公开日榜 |
| 开源关注 | 185,141 Stars · ollama/ollama | 本站固定跟踪的 6 个项目 |
| 文本模型下载 | 24,162,298 · Qwen/Qwen3-0.6B | HF 文本生成类，近 30 日滚动量 |

来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。

## 最新一期 · 2026-10-29

**前沿模型、智能体工具与企业部署继续扩展**

本期核实 10 条新进展，覆盖网络安全模型、开源工具、企业工作流、语音 AI 与云业务。

每日精选，第 005 期。收录范围：2026-10-28 09:00 至 2026-10-29 09:00（Asia/Singapore）；原文仅标日期者保留日期精度。
实际首次整理：2026-10-29 09:05 UTC+8。
指标按实际保存的批次与采集时间查看。

## 1. Google 发布 Gemini 4 Carbon，先向网络安全防御人员开放

![Carbon 首批能力与开放阶段。漏洞发现：88.2%，SEC-bench Pro，Google 公布；漏洞利用：54.8%，ExploitGym，Google 公布；漏洞修补：71.0%，CWE-bench，Google 公布；当前开放：部分防御者，开发者和消费者尚待后续推出](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/gemini-4-carbon.svg)

安全评测数值为 Google 公布结果；外部访问当前受限。

Google DeepMind 于 10 月 28 日公布 Gemini 4 Carbon，称其面向长周期工程任务及网络安全防御。

Google 列出的 SEC-bench Pro、ExploitGym 与 CWE-bench 成绩分别为 88.2%、54.8% 与 71.0%；Carbon 目前按 Fairwind 计划分批提供给部分网络安全防御人员，面向开发者和消费者的开放仍在后续安排中。

分类：模型；状态：已公布 · 受限预览启动；原文日期：2026-10-28。

来源：[Google DeepMind](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)

## 2. Meta 向五所美国高校提供模型与 200 万美元研究资助

![五校合作的研究方向。医学影像：心衰风险，用 CT、病历与 ECG 探索预测；婴儿护理：导管监测，识别气管导管移位与压力迹象；辅助沟通：失智症研究，研究适应认知差异的对话系统](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/meta-university-ai-research-2026-10-28.svg)

Meta 公告称提供模型访问与合计 200 万美元资助。

Meta 10 月 28 日宣布与加州理工、俄亥俄州立大学医学院、路易斯安那州立大学、印第安纳大学及 UTHealth Houston 合作，并向五校提供合计 200 万美元资助和最新模型访问。

项目包括监测婴儿气管切开导管移位、探索心衰风险预测，以及改善失智症患者交流等。Meta 的公告称，部分项目仍在开发或验证阶段；相关研究目标不等同于已经证明的临床效果。

分类：研究；状态：合作公布 · 项目研究中；原文日期：2026-10-28。

来源：[Meta Newsroom](https://about.fb.com/news/2026/10/meta-partners-with-five-us-universities-to-accelerate-medical-and-scientific-breakthroughs/)

## 3. Microsoft 将 Copilot 多模型 harness 开放给 Foundry 客户

![Copilot harness 位于模型与 Agent 之间。模型层：20+ 模型，支持多家模型及自带密钥；编排层：Copilot harness，指令、上下文、工具与执行控制；应用层：多种 Copilot，Code、Studio、CLI、VS Code 等](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/microsoft-copilot-harness-2026-10-28.svg)

微软称此编排层可管理上下文、工具、运行环境与控制。

Microsoft 10 月 28 日宣布，通过 Microsoft Foundry 提供 Copilot harness 的托管版本。该编排层负责为 Agent 配置指令、上下文、执行环境和控制，并支持 MCP、Agent Skills 与插件。

微软称该 harness 已用于 Copilot Code、Copilot Studio、GitHub Copilot 应用、CLI 和 VS Code 等产品，并支持 20 多种前沿模型及自带密钥。性能和用户规模数据来自公司自身介绍，实际选择仍取决于 Foundry 客户的配置与模型接入。

分类：产品；状态：已公布 · 通过 Microsoft Foundry 提供；原文日期：2026-10-28。

来源：[Microsoft Official Blog](https://blogs.microsoft.com/blog/2026/10/28/introducing-the-microsoft-copilot-harness-unlocking-the-potential-of-truly-multi-model-agentic-work/)

## 4. OpenAI 与 ServiceNow 扩大企业工作流合作

![企业工作流接入 ChatGPT 与 Codex。现已提供：ServiceNow MCP，可从 OpenAI 市场接入；2027 Q1：语音能力，语音描述并填写 AI 评估信息；2027 Q2：安全功能 GA，1 月预计开始早期访问；2027：Codex 集成，计划进入 AI Workflow Factory](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/openai-servicenow-enterprise-workflows-2026-10-28.svg)

MCP 插件已提供；其他合作功能按公告计划分期推出。

OpenAI 与 ServiceNow 10 月 28 日宣布扩大合作。用户未来可在 ChatGPT 中查询相似 IT 事件、评估变更风险并更新 ServiceNow 记录，组织可自行选择开放哪些操作，Action Fabric 将沿用既有业务规则与权限。

目前 ServiceNow MCP 插件已在 OpenAI 市场提供；安全能力预计 2027 年 1 月进入早期访问，第二季度计划一般开放，语音能力与 Codex 开发集成也在后续计划中。合作公告把多项能力标为未来安排，现阶段不应视作全部上线。

分类：产品；状态：合作扩展 · 插件已提供，其他能力分期推出；原文日期：2026-10-28。

来源：[OpenAI](https://openai.com/index/openai-servicenow-partnership-expansion/)

## 5. GitHub Agentic Workflows 正式可用，默认权限为只读

![从任务描述到 Agent 工作流。任务定义：Markdown，自然语言描述要自动化的任务；工作流生成：Actions YAML，编译为标准 GitHub Actions；Agent 执行：只读 + 沙箱，默认只读并隔离运行；变更检查：校验 + 扫描，应用前经过安全输出和威胁检测](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/github-agentic-workflows-ga-2026-10-28.svg)

GitHub 公告说明默认只读、沙箱执行及变更安全检查。

GitHub 10 月 28 日宣布 Agentic Workflows 一般可用，用户可用自然语言 Markdown 描述问题分流、CI 失败分析或文档维护任务，再由工具生成标准 GitHub Actions YAML。工作流可选 Copilot 或自带编程 Agent，并复用现有 runner 与策略。

GitHub 称 Agent 默认采用只读权限，在沙箱容器和 Agent Workflow Firewall 中执行，输出还要经过安全校验与威胁检测。产品已面向 GitHub Free、Team 和 Enterprise 可用；使用默认 Copilot CLI 引擎需要 Copilot 许可。

分类：开源；状态：正式可用 · 支持 GitHub Free、Team、Enterprise；原文日期：2026-10-28。

来源：[GitHub Changelog](https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available/)

## 6. GitHub 开源 Replica：用团队设计系统生成交互原型

![Replica 将设计系统带入原型生成。输入规范：团队设计系统，组件、模式与设计文档；自然语言：提出原型想法，在 Copilot app 创建并迭代；协作评估：本地或 Hub，Hub 可自托管并分享反馈；许可：MIT，GitHub 已开源项目](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/github-replica-oss-ai-prototyping-2026-10-28.svg)

开源工具从团队组件与文档出发，产出交互原型供协作评估。

GitHub 10 月 28 日开源 Replica，团队可将设计系统组件、模式和文档作为生成约束，再用自然语言在 Copilot app 中创建与修改交互原型。

原型可以在本地试用，也可通过可选的自托管 Replica Hub 分享并收集反馈。工具目前是协助探索设计方案的原型流程，公告没有把生成结果描述为可直接投产的产品实现。

分类：开源；状态：开源发布 · MIT 许可；原文日期：2026-10-28。

来源：[GitHub Changelog](https://github.blog/changelog/2026-10-28-introducing-replica-an-open-source-ai-prototyping-tool/)

## 7. NVIDIA 发布 Nemotron 3.5 Transcribe，覆盖 40 种语言

![一个模型，多种转录方式。语言范围：40 种语言，支持语音识别与语音翻译；录音时长：最长 1 小时，可按需生成说话人词级时间戳；模型规模：约 4.3B 活跃参数，基于约 30B 总参数 MoE；权重格式：4 种格式，BF16、FP8、NVFP4、GGUF](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/nvidia-nemotron-35-transcribe-2026-10-28.svg)

模型权重公开；榜单准确率为 NVIDIA 自行报告的评测结果。

NVIDIA 10 月 28 日发布 Nemotron 3.5 Transcribe，模型支持逐字稿、书面形式、上下文转录、说话人标注、语音翻译与 40 种语言识别，单段录音最长一小时，并可按需输出说话人归属的词级时间戳。

NVIDIA 同时开放 BF16、FP8、NVFP4 与 GGUF 权重，并提供 NeMo Speech 微调工具包，许可证为 OpenMDW-1.1。其排行榜 WER、速度和精度数据均由 NVIDIA 报告，需结合具体测试集和部署硬件理解。

分类：开源；状态：开放权重发布 · OpenMDW-1.1；原文日期：2026-10-28。

来源：[NVIDIA Nemotron Research](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/)

## 8. Rime 推出可微调语音到语音模型 Prism

![企业语音模型的可控环节。部署：本地 / 私有云，企业可在自有基础设施运行；输出流程：先文本后语音，播出前可检查生成文字；企业试验：68% → 100%，订单确认与取货方式，Rime 报告；企业试验：66% → 88%，无长时间静默通话比例，Rime 报告](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/rime-prism-speech-2026-10-28.svg)

Revmo 对照数据由 Rime 新闻稿披露，未提供独立复核。

Rime 10 月 28 日通过新闻稿发布 Prism，称企业可在本地或私有云运行，并根据自身通话数据调整模型、词汇、发音和防护规则。该模型先生成文字，再输出语音，使企业可在播出前检查文本。

Rime 公布一项与 Revmo 的企业试验：订单确认与取货方式指标从 GPT 对照组的 68% 升至 100%，无长时间静默通话比例从 66% 升至 88%。数据来自公司披露的客户试验，新闻稿未提供完整实验设计或独立评测。

分类：产品；状态：已发布 · 企业试验数据由厂商披露；原文日期：2026-10-28。

来源：[Rime（PR Newswire）](https://www.prnewswire.com/news-releases/rime-launches-prism-the-first-fine-tunable-frontier-speech-to-speech-model-302922665.html)

## 9. 企业 AI 初创 Fragment 以 5600 万美元融资亮相

![采购异常处理的 Agent 流程。识别异常：订单 / 发票，汇集跨系统采购与付款问题；注入上下文：企业规则，关联政策、关系与内部知识；执行处理：授权操作，在现有系统中推进解决；已提及客户：Graybar + CNX，公司称已开始应用，未披露量化成效](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/fragment-funding-procurement-agent-2026-10-28.svg)

融资及客户应用信息来自 Fragment 新闻稿。

Fragment 10 月 28 日公开亮相并披露累计融资 5600 万美元，其中 A 轮由 8VC 领投，种子轮由 General Catalyst 与 A* 联合领投。公司产品面向大型制造、分销和能源企业采购，试图跨现有系统处理订单变更、发票差异及付款异常。

公司称平台已在 Graybar 和 CNX 开始应用，其代理会结合企业政策、关系和内部知识调查异常并执行获授权的处理步骤。公告未披露融资两轮的具体拆分金额或量化客户成效，相关自动化能力仍以公司与客户描述为主。

分类：产业；状态：公司亮相 · 累计融资 5600 万美元；原文日期：2026-10-28。

来源：[Fragment（GlobeNewswire）](https://www.globenewswire.com/news-release/2026/10/28/3390260/0/en/fragment-launches-with-56-million-to-automate-the-work-enterprise-software-leaves-behind.html)

## 10. Microsoft 财季收入增长 19%，Azure 增长 48%

![云业务继续扩张。季度营收：$92.3B，同比增长 19%；Microsoft Cloud：$63.9B，同比增长 30%；Azure：+48%，同比增长，公司未拆分 AI 贡献；商业履约义务：$677B，同比增长 73%](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/microsoft-fy27-q1-cloud-ai-2026-10-28.svg)

公司财报数据；Azure 增长不等同于 AI 收入增长。

Microsoft 10 月 28 日公布截至 9 月 30 日的 FY2027 第一季度业绩：营收 923 亿美元，同比增长 19%；Microsoft Cloud 营收 639 亿美元，同比增长 30%；Azure 营收同比增长 48%。

公司还披露商业剩余履约义务增至 6770 亿美元，同比增长 73%。这些数字为公司财报口径，业务增长覆盖多类云服务和订单，不可直接等同于 AI 收入或 AI 工作负载增幅。

分类：产业；状态：财报公布 · Azure 同比增长 48%；原文日期：2026-10-28。

来源：[Microsoft Investor Relations](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast)

**历史归档**

- [2026-10-29 · 前沿模型、智能体工具与企业部署继续扩展](archive/2026-10-29.md)
- [2026-10-28 · 模型研究、企业代理与 AI 基础设施的多线推进](archive/2026-10-28.md)
- [2026-10-27 · 企业 AI 加入流程与数据层，终端和资本市场出现新动作](archive/2026-10-27.md)
- [2026-10-26 · AI 正在进入工具、数据与日常工作](archive/2026-10-26.md)
- [2026-10-23 · 模型能力向前一步，工具与证据也要跟上](archive/2026-10-23.md)
