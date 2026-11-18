# Seven Tech Newsroom

每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。

[访问网站](https://caixypromise.github.io/seven-tech-newsroom/) · [RSS](https://caixypromise.github.io/seven-tech-newsroom/feed.xml) · [源码仓库](https://github.com/CaixyPromise/seven-tech-newsroom) · [作者主页](https://github.com/CaixyPromise) · [运行说明](OPERATIONS.md)

最近一期：2026-11-18。共 21 期、187 条独立记录；按实际发布状态与来源标时。

**最新数据快照**：2026-11-18 09:02 UTC+8；OpenRouter 日榜另截至 2026-10-31 UTC。

| 观察项 | 最新观测 | 范围 |
| --- | --- | --- |
| 模型基本费估算 | $0.00135 · MiniMax M3.1 Flash | 7 个选定模型，10K 输入 + 2K 输出 Token |
| 平台单日用量 | 约 7.09T Token · DeepSeek V4.1 Flash 1017 | OpenRouter 2026-10-31 UTC 公开日榜 |
| 开源关注 | 187,436 Stars · ollama/ollama | 本站固定跟踪的 6 个项目 |
| 文本模型下载 | 34,373,187 · openai-community/gpt2 | HF 文本生成类，近 30 日滚动量 |

来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。

## 最新一期 · 2026-11-18

**模型、企业 AI 与算力更新**

OpenAI 发布新模型并拓展法律与销售工具；Microsoft Ignite 带来模型、Windows 和 Azure 更新，Google Cloud 与 Orange 也公布新计划。

每日精选，第 021 期。收录范围：2026-11-17 09:00 至 2026-11-18 09:00（Asia/Singapore）。
实际首次整理：2026-11-18 09:02 UTC+8。
指标按实际保存的批次与采集时间查看。

## 1. OpenAI 发布 GPT-6.2 Astra 与 Sol，扩展工作与开发者可用范围

![两款模型与可用入口。GPT-6.2 Astra：复杂专业任务，ChatGPT Work、Codex 与 API；GPT-6.2 Sol：日常工作，ChatGPT Work、Codex 与 API；Astra API：$8 / $40，每百万输入 / 输出 Token](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/openai-gpt62-astsol-2026-11-17.svg)

模型定位与可用范围据 OpenAI 公告；性能数据为厂商或注明基准结果。

OpenAI 于 11 月 17 日发布 GPT-6.2 Astra 和 GPT-6.2 Sol，分别面向复杂专业任务与日常工作。公司称，两款模型在多步工作流中的输出效率有所提升，并已向 Plus、Pro、Enterprise、Edu 用户开放 ChatGPT Work 和 Codex；开发者也可通过 API 调用。

OpenAI 公布的评测和成本比较来自其内部测试或指定基准，不能直接视作所有任务的独立结果。Astra API 标准价为每百万输入 Token 8 美元、输出 40 美元，缓存输入为 0.40 美元；Sol 延续此前版本的单价。

分类：模型；状态：模型发布；原文日期：2026-11-17。

来源：[OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol/)

## 2. OpenAI 更新 Astra for Law，向企业客户开放申请

![更新内容与访问状态。法律索引：扩展 1/3+，相较 9 月小范围推出时；访问范围：Enterprise 可申请，通过 Trusted Access Program；API：纳入申请，需通过相应访问计划](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/openai-astra-law-2026-11-17.svg)

基准数字来自 OpenAI 引述的 Artificial Analysis 测试，不代表实际执业错误率。

OpenAI 于 11 月 17 日发布更新版 Astra for Law，并将访问申请扩大至所有 ChatGPT Enterprise 客户。该配置把 GPT-6.2 Astra 与法律检索索引和研究流程结合，API 访问也纳入 Trusted Access Program。

OpenAI 引述的 Artificial Analysis 比较显示，Astra for Law 在指定任务中的实质性幻觉数较低；这仍是特定基准的结果。法律研究需要逐项核对来源与适用法域，模型输出不能代替律师判断。

分类：产品；状态：企业申请开放（基准为厂商引用）；原文日期：2026-11-17。

来源：[OpenAI](https://openai.com/index/astra-law-6-2/)

## 3. ChatGPT for Sales 接入 CRM、会议与提案工具

![从客户研究到销售跟进。客户研究：筛选账户，结合 CRM 与外部信号；会前准备：简报与提案，汇集客户记录和会议内容；后续跟进：草拟行动，整理承诺、报价与下一步](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/openai-chatgpt-sales-2026-11-17.svg)

工作流程与合作插件范围据 OpenAI 公告；可用性依方案、地区和工作区设置而异。

OpenAI 于 11 月 17 日推出 ChatGPT for Sales，包含销售插件和 30 多款新增或扩展的合作插件，覆盖客户研究、会议准备、提案制作、CRM 信息和跟进等环节。公告列出的连接工具包括 Salesforce、HubSpot、Salesloft、Gong 等。

企业管理员可在工作区中启用相关插件，并决定成员能够连接的应用及操作权限。具体功能会按方案、地区和工作区设置变化，第三方服务本身也可能需要单独账户或订阅。

分类：产品；状态：产品发布（可用范围因方案而异）；原文日期：2026-11-17。

来源：[OpenAI](https://openai.com/index/introducing-chatgpt-for-sales/)

## 4. Microsoft Ignite 推出新 MAI 模型，覆盖编程、安全与多媒体

![新 MAI 模型覆盖的任务。编程：Code 2 / Flash，Copilot 可用，Flash 也有 Foundry 预览；网络安全：Cyber 2 Flash，面向防御和漏洞修复工作；图像与语音：Image 2.7 / Realtime 1，Foundry 与 MAI Labs 等入口；转录：Transcribe 2，用于 Dragon Copilot 医疗记录](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/microsoft-mai-models-ignite-2026-11-17.svg)

模型类别与产品可用状态据 Microsoft AI 公告，评测比较为厂商公布。

Microsoft 于 11 月 17 日在 Ignite 公布新一批 MAI 模型，覆盖编码、安全、图像、实时语音和转录等用途。MAI Code 2 已在 GitHub Copilot 提供，Code 2 Flash 也可在 Copilot 使用，并以有限预览形式进入 Foundry；图像模型则已在 Foundry 上线。

微软称其内部及指定基准测试显示，这些模型在部分任务上以较低价格接近或超过对照模型。相关比较由微软发布，任务范围和测试设置各异；例如 Code 2 主要针对日常企业编码，并未针对基础科学或超长程代理任务调优。

分类：模型；状态：模型发布（部分功能预览）；原文日期：2026-11-17。

来源：[Microsoft AI](https://microsoft.ai/news/microsoft-ignite-2026/)

## 5. Microsoft 联合 40 多家机构推进 AI 透明度倡议

![倡议的三项工作方向。标准协作：参与 NIST，推进透明度、安全与治理；行业参与：40+ 组织，包括科技、金融与汽车机构；产品落地：逐步纳入，Microsoft AI、Foundry 与 Copilot](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/microsoft-ai-transparency-initiative-2026-11-17.svg)

这是跨行业倡议；统一标准仍在协作制定中。

Microsoft 于 11 月 17 日宣布 AI Transparency Initiative，称正与 40 多家组织合作，推动跨模型、跨供应商的透明度、安全与治理方法。参与方包括 Accenture、Adobe、KPMG、Mastercard 和 Volvo Cars。

倡议计划扩大对 NIST 代理标准工作的参与，并探索如何记录代理访问的数据和采取的行动，让组织在模型或供应商变化后仍能审查证据。现阶段这是标准和协作倡议，微软表示也会把相关做法逐步纳入自家产品。

分类：治理；状态：行业倡议启动；原文日期：2026-11-17。

来源：[Microsoft Source](https://news.microsoft.com/source/2026/11/17/microsoft-and-organizations-across-industries-launch-ai-transparency-initiative-to-strengthen-enterprise-trust-in-ai-models-and-agents/)

## 6. Microsoft 与 Salesforce 推出 Copilotforce 连接方案预览

![CRM 上下文进入 Copilot。身份验证：MCP 访问，使用现有 Salesforce 权限；工作上下文：CRM + M365，结合客户记录与沟通材料；产品状态：公开预览，Sales Cloud in Teams 仍在试点](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/microsoft-salesforce-copilotforce-2026-11-17.svg)

Salesforce in Copilot 为公开预览；访问和操作仍受 Salesforce 原有权限控制。

Microsoft 与 Salesforce 于 11 月 17 日公布 Copilotforce 合作，把 Salesforce 客户上下文及部分销售操作接入 Microsoft 的 AI 工作体验。Salesforce in Copilot 通过经过验证的 MCP 访问，销售人员可在 Salesforce 现有权限范围内查看记录并执行支持的业务操作。

Salesforce in Copilot 从当天起进入公开预览。Microsoft OneLake 与 Salesforce Data 360 之间的数据共享则分别处于正式提供和公开预览阶段；Sales Cloud in Teams 仍在企业试点，后续开放测试尚未开始。

分类：产品；状态：公开预览与企业试点；原文日期：2026-11-17。

来源：[Microsoft Source](https://news.microsoft.com/source/2026/11/17/microsoft-and-salesforce-announce-copilotforce-bringing-trusted-customer-context-and-action-into-microsoft-ai-experiences/)

## 7. Windows 扩展代理隔离，并预览本地模型路由

![代理与本地 AI 的推出阶段。已正式提供：容器学习与宽松模式，在执行限制前观察代理行为；预览：Fusion 本地模型路由，GitHub Copilot 调用开发者电脑模型；后续推出：Copilot+ PC 本地能力，上下文、操作和模型尚未上线](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/microsoft-windows-hybrid-intelligence-ignite-2026-11-17.svg)

按 Microsoft 公告区分正式提供、预览及尚未推出的能力。

Microsoft 于 11 月 17 日公布 Windows 面向代理计算的新进展，包括 Microsoft Execution Containers 的隔离能力、Windows 365 for Agents，以及 GitHub Copilot Fusion 在开发者电脑上调用本地模型的预览功能。Windows Server 2028 也已进入公开预览。

这些更新的阶段并不相同：部分容器管理模式已正式提供，Copilot Fusion 本地模型路由仍在预览，Copilot+ PC 的本地上下文和操作能力则尚未推出。对企业而言，代理隔离、身份和权限管理仍是部署条件的一部分。

分类：产品；状态：多项更新（正式、预览与计划并存）；原文日期：2026-11-17。

来源：[Windows Experience Blog](https://blogs.windows.com/windowsexperience/2026/11/17/microsoft-ignite-2026-building-windows-for-the-next-era-of-work/)

## 8. Azure Cobalt 200 虚拟机正式开放，首批覆盖 14 个区域

![开放范围与扩展计划。当前：14 个区域，Cobalt 200 虚拟机正式提供；2026 年底：计划 23 个区域，微软公布的扩展目标；性能：最高 +50%，相对 Cobalt 100，厂商数据](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/azure-cobalt200-ga-2026-11-17.svg)

性能数据和区域计划来自 Microsoft Azure 公告。

Microsoft 于 11 月 17 日宣布 Azure Cobalt 200 虚拟机正式提供，首批覆盖 14 个区域。微软称，其相对 Cobalt 100 性能最高提升 50%，并计划在 2026 年底前扩展至 23 个区域。

这些 Arm 虚拟机面向云原生、数据密集型和代理式 AI 工作负载，微软还表示计划从 2027 年起让其成为新增 Azure 计算容量的重要组成。性能提升数字来自微软公布的产品数据，实际收益会随工作负载和配置而变化。

分类：基础设施；状态：正式提供（14 个区域）；原文日期：2026-11-17。

来源：[Microsoft Azure](https://azure.microsoft.com/en-us/blog/azure-cobalt-200-vms-now-available-proven-on-real-workloads-and-built-for-the-agentic-era/)

## 9. Google Cloud 为欧洲受监管 AI 初创公司开设加速器

![Sovereign AI 加速器。申请范围：欧洲与以色列，受监管行业 AI 初创团队；项目周期：15 周，线上与线下混合辅导；费用条件：免股权，不收取参与公司股权；申请截止：2027-01-15，Google 公布的最后申请日](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-sovereign-ai-accelerator-2026-11-17.svg)

项目条件、期限与申请日期据 Google Cloud 公告。

Google Cloud 于 11 月 17 日启动 Google for Startups Accelerator: Sovereign AI 招募，面向欧洲和以色列、开发受监管行业 AI 产品的初创公司。入选团队将参加为期 15 周的混合项目，获得 Google 工程师辅导、架构支持和监管沙盒准备建议。

项目不收取股权，重点面向政府服务、医疗、金融和网络安全等领域，申请截止日期为 2027 年 1 月 15 日。Google 表示将支持团队在其分层主权云方案中部署；这属于创业支持计划，不代表监管认证或产品合规背书。

分类：产业；状态：开放申请；原文日期：2026-11-17。

来源：[Google Cloud](https://cloud.google.com/blog/topics/startups/sovereign-ai-on-your-terms-our-new-startup-accelerator-is-open)

## 10. Orange 发布五款支持沃洛夫语的开放权重模型

![沃洛夫语模型资源。模型数量：5 款，经微调的开放权重大语言模型；语言任务：理解与生成，针对沃洛夫语文本；使用许可：非商业用途，商业使用可能需另签协议](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/orange-wolof-models-2026-11-17.svg)

模型用途与许可来自 Orange 公告；商业使用可能需另行授权。

Orange 于 11 月 17 日发布五款支持沃洛夫语的微调大语言模型，并在 Hugging Face 提供模型权重和配套训练数据。公司称，模型可处理沃洛夫语文本理解与生成；训练数据基于公开数据自动翻译，不含 Orange 企业数据。

资源目前可免费用于非商业用途，商业使用可能需要与 Orange 另行签订协议。发布开放权重有助于研究者和开发者开展本地语言实验，但模型在不同方言、口语和实际服务中的表现仍需独立验证。

分类：开源；状态：开放权重发布（非商业用途）；原文日期：2026-11-17。

来源：[Orange Newsroom](https://newsroom.orange.com/orange-releases-african-language-ai-models-to-advance-digital-inclusion-in-africa/?lang=eng)

## 11. Orange Business 为 Live Intelligence 增加法国托管保护模式

![两种模式的数据处理边界。Protected Mode：法国托管与运营，模型、代理、数据和文档留在 Orange 环境；Open Mode：外部欧洲基础设施，可选择欧洲或瑞士部署的模型](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/orange-live-intelligence-protected-mode-2026-11-17.svg)

服务模式的托管地点与数据处理描述据 Orange 公告，实际范围应查阅合同和配置。

Orange Business 于 11 月 17 日为 Live Intelligence 推出 Protected Mode，供需要更高数据控制的业务场景使用。Orange 表示，启用后所用模型、代理、数据和文档都留在其于法国托管和运营的环境内，该模式当天起向所有客户提供。

平台同时保留 Open Mode，以使用部署在欧洲或瑞士外部基础设施上的模型。两种模式提供不同的数据处理边界；企业仍需核对服务配置、合同和具体工作流，不能只凭“法国托管”推断所有合规要求均已满足。

分类：产品；状态：产品上线；原文日期：2026-11-17。

来源：[Orange Newsroom](https://newsroom.orange.com/orange-business-launches-protected-mode-for-live-intelligence-giving-organizations-greater-choice-over-their-ai-environment/?lang=eng)

**历史归档**

- [2026-11-18 · 模型、企业 AI 与算力更新](archive/2026-11-18.md)
- [2026-11-17 · 模型发布、Agent 产品与 AI 基建治理](archive/2026-11-17.md)
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
