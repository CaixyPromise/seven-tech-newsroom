# Seven Tech Newsroom

每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。

[访问网站](https://caixypromise.github.io/seven-tech-newsroom/) · [RSS](https://caixypromise.github.io/seven-tech-newsroom/feed.xml) · [源码仓库](https://github.com/CaixyPromise/seven-tech-newsroom) · [作者主页](https://github.com/CaixyPromise) · [运行说明](OPERATIONS.md)

最近一期：2026-11-03。共 7 期、63 条独立记录；按实际发布状态与来源标时。

**最新数据快照**：2026-10-29 09:03 UTC+8；OpenRouter 日榜另截至 2026-10-31 UTC。

| 观察项 | 最新观测 | 范围 |
| --- | --- | --- |
| 模型基本费估算 | $0.002 · Claude Haiku 5.5 | 7 个选定模型，10K 输入 + 2K 输出 Token |
| 平台单日用量 | 约 7.09T Token · DeepSeek V4.1 Flash 1017 | OpenRouter 2026-10-31 UTC 公开日榜 |
| 开源关注 | 185,141 Stars · ollama/ollama | 本站固定跟踪的 6 个项目 |
| 文本模型下载 | 24,162,298 · Qwen/Qwen3-0.6B | HF 文本生成类，近 30 日滚动量 |

来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。

## 最新一期 · 2026-11-03

**模型、算力基础设施与企业 AI 应用继续推进**

本期补齐两日窗口，整理 11 条来自官方公告、企业技术文章与开源项目的进展，涉及模型评测、能源与云基础设施、企业软件及 AI 部署。

每日精选，第 007 期。收录范围：补齐窗口：2026-11-01 09:00 至 2026-11-03 09:00（Asia/Singapore）；原文仅标日期者保留日期精度。
实际首次整理：2026-11-03 09:03 UTC+8。
指标按实际保存的批次与采集时间查看。

## 1. 美团发布 LongCat-2.5：面向长程智能体任务的多模态模型

![LongCat-2.5 发布信息。总参数：1.6 万亿，美团公告所列规模；模型形态：原生多模态，发布方产品定位；任务方向：长程智能体，公告描述的目标场景；训练算力：国产算力，美团公告披露](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/meituan-longcat-25-2026-11-02.svg)

模型规模与定位据美团公告；评测结果为发布方披露。

美团 11 月 2 日发布 LongCat-2.5，将其定位为面向长程智能体任务的原生多模态模型。公司公告称，模型总参数为 1.6 万亿，训练全程使用国产算力。

美团还公布了模型介绍和评测结果；这些性能数字属于发布方披露，不能直接视为独立复测。现有公告将 LongCat-2.5 描述为能力发布，实际开放范围和使用条件应以模型页面及服务入口为准。

分类：模型；状态：公司发布；性能数据为发布方披露；原文日期：2026-11-02。

来源：[美团](https://www.meituan.com/news/NN261102280001343)
来源：[LongCat](https://longcat.ai/blog/longcat-2.5)

## 2. NVIDIA 开源 Workload Map，统一描述 Kubernetes AI 工作负载

![统一工作负载描述的用法。输入定义：CRD + YAML，声明工作负载结构与状态；共享解析：Go 库，读取模板、副本与层级；项目目录：13 类示例，包含 JobSet、Ray 与 KServe](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/nvidia-workload-map-2026-11-02.svg)

按 NVIDIA 技术文章说明；Workload Map 采用 Apache 2.0 许可。

NVIDIA 11 月 2 日介绍开源组件 Workload Map，用统一结构描述 Kubernetes 上不同框架的分布式工作负载。该项目以 CRD、Go 库和声明式定义记录工作节点、模板、副本数与状态，让调度器和平台能够复用同一份框架描述。

NVIDIA 表示，目录已包含 JobSet、PyTorchJob、RayCluster、KServe 和 NVIDIA Dynamo 等工作负载定义，并称该组件采用 Apache 2.0 许可、已用于 Run:ai。它降低的是各平台重复编写解析适配器的需要，具体兼容范围仍取决于项目目录和使用者实现。

分类：开源；状态：开源组件；NVIDIA 技术文章介绍；原文日期：2026-11-02。

来源：[NVIDIA Developer Blog](https://developer.nvidia.com/blog/support-new-ai-frameworks-faster-using-nvidia-workload-map/)

## 3. OpenAI 发布 LifeVal，评估 AI 完成日常事务的能力

![LifeVal 评测构成。受访者：3,995 人，OpenAI 公布的代表性调查；幼儿园筛选：93.1%，页面展示的任务得分；洪水准备：98.0%，页面展示的任务得分；任务领域：7 类，照护、健康至政府服务](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/openai-lifeval-2026-11-02.svg)

样本与示例分数据 OpenAI 页面；成绩由发布方报告。

OpenAI 11 月 2 日公布 LifeVal，称这是用于评估 AI 完成日常生活任务的基准，覆盖照护、健康、教育、家庭管理、个人理财、购物和政府服务等领域。该公司先参考美国及跨国时间利用调查，再对 3,995 名受访者进行具有代表性的调查，以筛选人们希望 AI 协助的任务。

OpenAI 展示了若干自家模型在特定任务中的得分，例如幼儿园筛选为 93.1%、洪水准备志愿者安排为 98%。这些数字由 OpenAI 公布，页面未提供足以替代独立复测的跨机构结果；LifeVal 当前更适合作为其评测方法和任务样例来阅读。

分类：研究；状态：公司发布的评测方法；示例成绩为发布方数据；原文日期：2026-11-02。

来源：[OpenAI](https://openai.com/index/lifeval/)

## 4. OpenAI 推出 Grid Protectors 计划，提出数据中心削峰安排

![计算园区与电网需求响应。计划：Grid Protectors，与公用事业及监管方协作；协议上限：1,000 MW，Georgia Power 于 2026 年 7 月披露的协议上限；试点阶段：开发中，Effingham County 园区尚未运营](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/openai-grid-protectors-2026-11-02.svg)

1,000 兆瓦协议来自 2026 年 7 月公告；Effingham 园区尚在开发。

OpenAI 11 月 2 日宣布 Grid Protectors 计划，称将与公用事业公司、监管机构和政策制定者合作，为未来计算园区制定在电网紧张时降低用电的安排。公司以佐治亚州 Effingham County 的项目为例；该园区仍在开发，且此前已与 Georgia Power 签订灵活需求响应协议。

Georgia Power 在 2026 年 7 月的公告中曾披露，协议包含最高 1,000 兆瓦的灵活需求响应，具体是高峰期由电力公司调低对该设施的供电。这个数字不是 11 月 2 日新签的承诺，也不是已经实现的节电量；OpenAI 将该项目作为 Grid Protectors 的实践方向，未来效果仍取决于园区建设和电网运行。

分类：基础设施；状态：计划公布；佐治亚试点仍在开发；原文日期：2026-11-02。

来源：[OpenAI](https://openai.com/index/grid-protectors-program/)
来源：[Georgia Power](https://www.georgiapower.com/news-hub/press-releases/georgia-power-to-serve-openai-project-in-effingham-county.html)

## 5. OpenAI 介绍 Pando：支撑其单体仓库的 Git 后端

![Pando 的内部运行数据。部署范围：全公司开发，OpenAI 单体仓库；推送延迟：近 5 倍降低，生产环境中位数；数据传输：近 1 PB / 日，OpenAI 报告的 Git 数据量](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/openai-scaling-git-pando-2026-11-02.svg)

以下指标为 OpenAI 对自有生产系统的披露。

OpenAI 11 月 2 日介绍其内部 Git 后端 Pando。公司称，随着 Codex 带来更多并行分支、推送和构建任务，原有单体仓库服务逐渐遇到读写瓶颈；Pando 保留 Git 协议和客户端兼容性，目前已支撑 OpenAI 的全部开发工作。

按 OpenAI 公布的数据，Pando 将生产环境中的推送中位延迟降低近 5 倍，每天传输接近 1 拍字节的 Git 数据。以上是公司内部系统的数据，文章称 OpenAI 会继续向 Git 生态贡献改进，但没有说 Pando 已作为可安装产品公开发布。

分类：基础设施；状态：公司内部系统已部署；性能为公司披露；原文日期：2026-11-02。

来源：[OpenAI](https://openai.com/index/scaling-git-at-openai/)

## 6. 阿布扎比与 OpenAI 签署四项协议，政府 AI 监管试点已投产

![四项合作的落点。政府：机器可读规则，食品进口试点已投产；能源：ADNOC，能源业务 AI 合作；投资：Mubadala，投资分析与风险评估；AI 采用：五年合作，OpenAI 与 Inception42](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/abu-dhabi-openai-agreements-2026-11-02.svg)

据阿布扎比媒体办公室公告；监管试点仍由政府人员作最终决定。

阿布扎比媒体办公室 11 月 2 日公布，阿布扎比政府实体与 OpenAI 签署四项政府、能源和投资领域协议。政府项目之一是 Machine-Readable Government，将部分政策和法规转换为机器可读形式，协助官员进行合规评估；首个聚焦食品进口的试点已在阿布扎比农业与食品安全局投产。

官方资料称，相关评估可追溯到所依据的规则，最终决定仍由政府人员负责。协议还涉及 ADNOC 能源业务、Mubadala 投资分析，以及 OpenAI 与 Inception42 的五年 AI 采用合作；官方称推理由阿联酋境内数据中心承担。上述进展来自参与方公告，项目覆盖范围和后续扩展仍待执行。

分类：产业；状态：政府公告；首个监管辅助试点已投产；原文日期：2026-11-02。

来源：[Abu Dhabi Media Office](https://www.mediaoffice.abudhabi/en/crown-prince-news/khaled-bin-mohamed-bin-zayed-meets-sam-altman-and-witnesses-signing-of-agreements-with-openai/)
来源：[Inception42](https://inception42.ai/news/inception42-open-ai-adnoc-and-mubadala-sign-strategic-partnerships)

## 7. Marvell 拟以全股票交易收购 Lumentum，瞄准 AI 光互连

![收购协议关键条款。交易方式：全股票，Marvell 收购 Lumentum；隐含企业价值：约 1,150 亿美元，公告所列交易估值；换股比例：4.5 : 1，每股 Lumentum 换 4.5 股 Marvell；当前阶段：待交割，已签最终协议](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/marvell-lumentum-acquisition-2026-11-02.svg)

交易与换股数据据公司公告；交割仍待完成。

Marvell 与光器件厂商 Lumentum 11 月 2 日宣布签署最终收购协议，Marvell 将以全股票方式收购 Lumentum。公告给出的交易隐含企业价值约 1,150 亿美元；按协议，Lumentum 股东每股可换取 4.5 股 Marvell 普通股。

两家公司称，合并后希望把 Marvell 的互连、交换和定制芯片能力，与 Lumentum 的激光器、光收发器及光交换技术结合，用于 AI 数据中心的电互连和光互连。交割尚未完成，公告提及的市场规模、协同和产品路线均属公司预期，不是已实现结果。

分类：产业；状态：已签最终协议；交易待完成；原文日期：2026-11-02。

来源：[Marvell](https://investor.marvell.com/_assets/_4b2ef940d8378f4928a6a90255e70f76/marvell/news/2026-11-02_Marvell_and_Lumentum_to_Combine_Creating_a_1040.pdf)

## 8. NetApp 完成 PEAK:AIO 收购，补充 AI 存储元数据技术

![收购带来的技术方向。已完成：PEAK:AIO 收购，NetApp 于 11 月 2 日宣布；技术：元数据 + 并行文件，并发与命名空间架构；后续方向：ONTAP / Novus，整合计划未承诺交付时间](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/netapp-peak-aio-acquisition-2026-11-02.svg)

收购已完成；产品集成与发布时间尚未承诺。

NetApp 11 月 2 日宣布完成对英国 AI 存储软件公司 PEAK:AIO 的收购。NetApp 表示，收购将把 PEAK:AIO 的元数据服务和并行命名空间技术带入其 ONTAP 数据架构，面向 AI 云和 GPU 云服务商的数据密集型工作负载。

公司称，这项技术旨在帮助存储系统处理更高并发与更大命名空间，并提到未来可能用于 NetApp Novus 等能力；公告同时明确，后续产品的开发、整合和推出时间并未承诺。此次收购已完成，所述新功能仍是产品方向。

分类：基础设施；状态：收购完成；产品整合未承诺；原文日期：2026-11-02。

来源：[NetApp](https://www.netapp.com/newsroom/press-releases/news-rel-20261102-492821/)

## 9. CrowdStrike 与 CoreWeave 扩大合作，为 AI 云提供安全服务

![AI 云安全合作覆盖。防护对象：云、容器、GPU，生产 AI 工作负载；安全服务：24/7 威胁搜寻，Falcon 专家服务；响应：托管检测响应，调查、遏制与修复；模型基础设施：SafeMind，CoreWeave 支持训练与推理](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/crowdstrike-coreweave-ai-security-2026-11-02.svg)

服务范围由 CrowdStrike 公告披露。

CrowdStrike 与 CoreWeave 11 月 2 日宣布扩大合作，为在 CoreWeave 云上运行关键 AI 工作负载的客户提供 Falcon 平台防护和全天候托管安全服务。方案覆盖云工作负载、容器和 GPU 集群，并包含威胁搜寻以及检测、调查和响应。

两家公司还表示，CoreWeave 为 CrowdStrike 的 SafeMind 安全模型提供训练与推理基础设施。公告描述的是双方联合提供的商业安全服务，没有披露独立客户成效或统一的部署范围，用户实际可用条件仍需向服务方确认。

分类：治理；状态：合作扩大；服务范围据厂商公告；原文日期：2026-11-02。

来源：[CrowdStrike](https://crowdstrike.gcs-web.com/news-releases/news-release-details/coreweave-partners-crowdstrike-secure-mission-critical-ai)

## 10. Lumen 与微软扩大合作，计划共同销售企业 AI 网络服务

![AI 网络合作的当前状态。当前：Alkira 已上架，Microsoft Marketplace 采购选项；合作方式：联合销售，共同规划企业客户机会；未来计划：更多 Azure 能力，范围与时间尚未公布](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/lumen-microsoft-ai-ready-networks-2026-11-02.svg)

Marketplace 上的 Alkira 已可采购；其余扩展仍为计划。

Lumen 与微软 11 月 2 日宣布扩大合作，计划共同面向企业销售网络服务，并在客户规划中结合网络现代化、Azure 迁移和 AI 基础设施需求。Lumen 表示，将推动旗下云网络与应用连接服务进入 Azure 及微软云生态。

公告提到 Alkira 已可通过 Microsoft Marketplace 采购；其他能力进入 Azure 或 Marketplace 仍是双方计划，尚未逐项说明时间和可用范围。合作重点是连接分布在公有云、私有数据中心和办公地点的数据与应用，并未披露新增网络覆盖或客户成效数据。

分类：基础设施；状态：合作扩大；部分能力仍属计划；原文日期：2026-11-02。

来源：[Lumen](https://ir.lumen.com/news/news-details/2026/Lumen-and-Microsoft-Expand-Collaboration-to-Co-Sell-Enterprise-AI-Ready-Networks/default.aspx)
来源：[Microsoft Source](https://news.microsoft.com/source/?section=materials)

## 11. HCLTech 推出 AI 主机运维服务，强调人员监督

![AI 主机运维服务组成。服务对象：关键主机环境，企业核心系统运维；AI 组件：技能代理 + 对话助手，协助系统管理与流程处理；人工控制：人员监督，公告说明的服务边界](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/hcltech-ai-mainframe-operations-2026-11-02.svg)

服务与人工监督描述据 HCLTech 公告；独立成效数据未公布。

HCLTech 11 月 2 日发布面向大型主机环境的 AI-Powered Operations 服务，目标是协助企业管理关键系统中的日常运维、可观测性和优化工作。公司介绍，该方案组合主机技能代理与对话式 AI 助手，并由专门的 Mainframe Center of Excellence 提供领域支持。

HCLTech 表示，服务用于提升运维效率和加快问题处理，但没有公布可独立核验的客户效果数据。公告明确将人员监督纳入方案；目前发布的是服务项目，具体客户部署、自动化权限和成效需结合合同及现场实施确认。

分类：产品；状态：服务发布；成效数据未披露；原文日期：2026-11-02。

来源：[HCLTech](https://www.hcltech.com/press-releases/hcltech-launches-ai-powered-operations-mainframe-environments)

**历史归档**

- [2026-11-03 · 模型、算力基础设施与企业 AI 应用继续推进](archive/2026-11-03.md)
- [2026-11-01 · 开放模型、智能体与安全机制迎来新进展](archive/2026-11-01.md)
- [2026-10-29 · 前沿模型、智能体工具与企业部署继续扩展](archive/2026-10-29.md)
- [2026-10-28 · 模型研究、企业代理与 AI 基础设施的多线推进](archive/2026-10-28.md)
- [2026-10-27 · 企业 AI 加入流程与数据层，终端和资本市场出现新动作](archive/2026-10-27.md)
- [2026-10-26 · AI 正在进入工具、数据与日常工作](archive/2026-10-26.md)
- [2026-10-23 · 模型能力向前一步，工具与证据也要跟上](archive/2026-10-23.md)
