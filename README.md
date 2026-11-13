# Seven Tech Newsroom

每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。

[访问网站](https://caixypromise.github.io/seven-tech-newsroom/) · [RSS](https://caixypromise.github.io/seven-tech-newsroom/feed.xml) · [源码仓库](https://github.com/CaixyPromise/seven-tech-newsroom) · [作者主页](https://github.com/CaixyPromise) · [运行说明](OPERATIONS.md)

最近一期：2026-11-13。共 17 期、150 条独立记录；按实际发布状态与来源标时。

**最新数据快照**：2026-11-12 09:55 UTC+8；OpenRouter 日榜另截至 2026-10-31 UTC。

| 观察项 | 最新观测 | 范围 |
| --- | --- | --- |
| 模型基本费估算 | $0.001568 · DeepSeek V4.1 Flash 1017 | 7 个选定模型，10K 输入 + 2K 输出 Token |
| 平台单日用量 | 约 7.09T Token · DeepSeek V4.1 Flash 1017 | OpenRouter 2026-10-31 UTC 公开日榜 |
| 开源关注 | 186,707 Stars · ollama/ollama | 本站固定跟踪的 6 个项目 |
| 文本模型下载 | 32,612,915 · openai-community/gpt2 | HF 文本生成类，近 30 日滚动量 |

来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。

## 最新一期 · 2026-11-13

**模型进入产品，AI 基础设施继续扩张**

本期聚焦 Gemini 4 Hydrogen、智能眼镜与创作工具更新，也关注企业代理运行环境、Trainium 推理支持和数据中心供应链。

每日精选，第 017 期。收录范围：2026-11-12 09:00 至 2026-11-13 09:00（Asia/Singapore）；原文仅标日期的条目保留日期精度。。
实际首次整理：2026-11-13 15:10 UTC+8。
指标按实际保存的批次与采集时间查看。

## 1. Google 推出 Gemini 4 Hydrogen，并扩展至搜索与开发工具

![Hydrogen 的发布范围与价格。模型定位：日常编码与代理，Google 描述的目标工作流；上下文：100 万 Token，Gemini API 模型上下文；输入价格：$1.50 / 百万 Token，Google 公布的 API 标价；输出价格：$7.50 / 百万 Token，Google 公布的 API 标价](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-gemini-4-hydrogen-2026-11-12.svg)

Google 公告所述；性能比较为厂商自报，具体产品推出范围有差异。

Google 于 11 月 12 日发布 Gemini 4 Hydrogen，定位为处理日常编码和代理工作流的快速模型，并称其已开始覆盖 Gemini 应用、Google 搜索、Gemini API、AI Studio、Android Studio 和企业产品。Google 同日还宣布将 Hydrogen 用于全球搜索，改善多步骤问题理解，并提供更多结构化回答、图片和链接。

Google 给出的基准成绩、速度和安全性比较来自公司公布的测试；模型标价为每百万输入 Token 1.50 美元、输出 7.50 美元，覆盖 100 万 Token 上下文。实际可用范围因产品和订阅层级而异，搜索功能的推出也不代表每位用户会在同一时间看到完全相同的体验。

分类：模型；状态：官方发布；分批推出；原文日期：2026-11-12。

来源：[Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)
来源：[Google](https://blog.google/products-and-platforms/products/search/gemini-4-hydrogen-search-upgrade/)

## 2. Google Flow 新增五款 AI 影像创作工具

![五项影像创作工具。Character Poster：角色海报，建立统一视觉风格；Character Arc：角色发展，呈现不同年龄与阶段；Pixel Machine：复古数字风格，生成像素化影像效果；Lucid Glass：光学折射效果，模拟棱镜、光晕与折射；Pocket Studio：单镜头多角度，由手机素材生成多机位画面](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-flow-creative-tools-2026-11-12.svg)

功能名称与描述来自 Google Flow 公告。

Google 于 11 月 12 日为 AI 创作工具 Flow 推出五项功能：Character Poster 用于制作风格统一的角色海报，Character Arc 展示角色跨年龄阶段的变化，Pixel Machine 提供复古数字视觉，Lucid Glass 模拟棱镜和光线折射，Pocket Studio 则可将手机拍摄素材生成多个镜头角度。

Google 表示这些工具由创作者参与设计，用户可以在 Flow 中试用。Pocket Studio 等功能会生成或修改影像内容，官方介绍强调保持原表演，但公告没有提供独立画质评测或各地区、账户层级的完整可用范围。

分类：产品；状态：官方发布；原文日期：2026-11-12。

来源：[Google](https://blog.google/innovation-and-ai/models-and-research/google-labs/new-google-flow-tools/)

## 3. Google 智能眼镜开放预订，12 月起发售

![预订、规格与首发条件。Warby Parker：起价 $395，美国及韩国系列之一；Gentle Monster：起价 $449，共推出六种设计；重量与续航：约 41 克 / 最长 9 小时，续航会随设置和使用变化；首发销售：12 月 10 日，美国、韩国 Google 账户可用](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-intelligent-eyewear-preorder-2026-11-12.svg)

价格、规格、地区和发售安排以 Google 公告为准。

Google 于 11 月 12 日为与 Warby Parker、Gentle Monster 和 Samsung 合作设计的智能眼镜开放预订。Warby Parker 系列起价 395 美元，Gentle Monster 系列起价 449 美元，官方称眼镜约重 41 克、续航最长约 9 小时，预计 12 月 10 日在线上及门店开售。

眼镜接入 Gemini，可通过语音或触控获取视觉描述、翻译和日常协助；Google 还公布摄像头指示灯、关闭开关及人脸遮挡等隐私设计。首发使用限美国和韩国 Google 账户，部分辅助功能需兼容 Android 手机，Guided Vision 也不是医疗或导航设备。

分类：产品；状态：预订开放；计划 12 月 10 日发售；原文日期：2026-11-12。

来源：[Google](https://blog.google/innovation-and-ai/technology/xr-ar/google-intelligent-eyewear-collections-pre-order/)
来源：[Google](https://blog.google/innovation-and-ai/technology/safety-security/intelligent-eyewear-privacy-protections/)

## 4. Google.org 为新一届博士研究员投入 1300 万美元

![博士研究项目资助方向。本届资金：$13 million，Google.org 公布的总额；研究方向：AI 与芯片，包括模型推理和硬件设计；其他主题：健康与量子，亦涉及语言与无障碍技术；项目累计：1,100+ 人，Google 称自 2009 年以来](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-phd-fellows-funding-2026-11-12.svg)

资金与历年支持人数为 Google 公布数据。

Google.org 于 11 月 12 日公布 2026 年 Google PhD Fellows 项目，为新一届全球博士研究员提供总计 1300 万美元支持。Google 表示，项目除资金外还提供计算资源及与公司研究人员交流的机会，研究主题涉及 AI、芯片、量子科学、健康和自然语言处理等领域。

这是面向早期研究人员的资助项目，不是新模型或商业产品发布。Google 称自 2009 年以来该项目已支持超过 1100 名研究生；这一累计数字和项目影响由主办方提供，公告未给出本届各地区的资金分配明细。

分类：产业；状态：项目资助公布；原文日期：2026-11-12。

来源：[Google](https://blog.google/company-news/outreach-and-initiatives/google-org/phd-fellows-2026/)

## 5. NFON 上线面向企业流程的 AI Agent Studio

![两种方式搭建业务代理。Agent Mode：自然语言描述，生成初版并通过对话测试；审核与回滚：用户确认变更，操作留痕且可撤销；Flow-Based Mode：可视化流程，配置条件和具体操作步骤](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/nfon-ai-agent-studio-2026-11-12.svg)

NFON 称产品已开放使用；具体部署由客户和合作伙伴实施。

德国企业通信服务商 NFON 于 11 月 12 日宣布 AI Agent Studio 已开放使用。企业可以用自然语言描述代理的任务和行为，由系统生成初始方案，再通过对话测试和修改；也可以在同一工作区用可视化流程配置条件与操作步骤。

NFON 表示，修改建议需要用户审阅批准，变更可追踪和撤销，产品通过其欧洲合作伙伴网络推广。公司列举的保险理赔接收、能源读数处理等是现有语音机器人的场景，不能据此认定新工具已在所有这些流程中完成部署。

分类：产品；状态：已开放使用（厂商公告）；原文日期：2026-11-12。

来源：[NFON AG](https://corporate.nfon.com/en/news/ir-news/corporate-news/nfon-adds-ai-agent-studio-to-its-ai-portfolio-2026-11-12-1200/)

## 6. Meta 扩大数据中心低碳材料与运输采购承诺

![四类供应链采购承诺。低碳水泥：至少 18 万吨，Sublime 协议支持的生产量；近零排放钢：Stegra 多年协议，支持瑞典项目扩产；电动货运：加州至亚利桑那，Nevoya 扩展 I-10 路线；再生塑料：年产 5,000 吨，MacroCycle 工厂目标产能](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/meta-low-carbon-datacenter-supply-2026-11-12.svg)

产能为协议支持或项目目标，不代表已经全部投产。

Meta 于 11 月 12 日公布一组多年采购承诺，涉及低碳水泥、近零排放钢材、电动货运和再生塑料，目标是支持数据中心建设供应链扩大相关产能。公司称，与 Sublime Systems 的协议至少支持 18 万吨低碳水泥生产，并帮助其建设首座商业规模工厂；与 MacroCycle 的协议则支持年产 5000 吨再生 PET 的工厂融资。

其他安排包括支持 Fortera 建设密苏里州新厂、与 Stegra 合作近零排放钢材，以及扩大 Nevoya 在加州和亚利桑那州的电动货运路线。相关产量和减排效果多为合作方项目计划或 Meta 的采购承诺，部分工厂尚在建设或扩产阶段。

分类：基础设施；状态：多年采购承诺；部分产能仍在规划或建设；原文日期：2026-11-12。

来源：[Meta](https://about.fb.com/news/2026/11/meta-new-agreements-clean-manufacturing-data-center-supply-chains/)

## 7. AWS 更新 AgentCore 运行时：会话启动更快并可缩至零

![新版运行时资源与启动指标。会话资源：8 vCPU / 32 GB，新版最高配置；容器镜像：最高 10 GB，硬件隔离会话支持；启动 P75：低于 2 秒，AWS 测试中的 2 GB 镜像；内存用量：最多降低 68%，AWS 对多轮会话的估算](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/aws-agentcore-runtime-v2-2026-11-12.svg)

性能数字来自 AWS 测试；旧运行时不会自动迁移。

AWS 于 11 月 12 日更新 Amazon Bedrock AgentCore Runtime，为每个会话保留独立硬件隔离的 Firecracker 微型虚拟机，并新增按需扩展至 8 个 vCPU、32 GB 内存及最高 10 GB 容器镜像的能力。闲置代理可缩至零，释放的内存会在数分钟内回收；新版也成为新建运行时的默认版本。

AWS 称，2 GB 镜像的会话在其测试中 P75 启动时间低于 2 秒，旧版为 29.7 秒，并估计多轮代理每会话内存用量最多可降 68%。已有运行时不会自动迁移；这些比较由 AWS 提供，客户仍需按地区、工作负载和计费条件验证实际收益。

分类：基础设施；状态：新版已开放；新建运行时默认采用；原文日期：2026-11-12。

来源：[AWS](https://aws.amazon.com/blogs/machine-learning/run-agents-securely-and-efficiently-with-the-next-generation-agentcore-runtime/)
来源：[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/new-agentcore-runtime-default/)

## 8. Natera 分享用 AI 代理辅助实验室设备运维的案例

![实验室设备运维代理案例。平均首响：17.4 小时 → 8 分钟，客户案例报告的变化；自动首响覆盖：96.2%，案例所述工单占比；评估范围：524 张工单，准确率评估只含部分工单；系统设计：2 个代理 + 技能库，后台诊断与工程师交互](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/aws-natera-swarm-agent-case-2026-11-12.svg)

AWS 与 Natera 报告的 90 天案例数据，非独立评测。

基因检测公司 Natera 与 AWS 于 11 月 12 日发布案例，介绍实验室运维系统 SWARM 如何用 Amazon Bedrock AgentCore 处理仪器故障工单。系统由后台诊断代理和工程师交互代理组成，共享技能库，并从设备手册、历史工单和运维数据中检索信息，生成诊断报告供工程师查看。

案例称，在 90 天生产评估中，平均首次响应由 17.4 小时降至约 8 分钟，524 张评估工单中 96.2% 获得自动首响；准确率比较仅覆盖其中有工程师确认结果的子集。数据由客户与云服务商共同发布，反映特定实验室配置，系统定位是补充工程师而非替代其判断。

分类：产业；状态：客户案例；厂商与客户自报评估；原文日期：2026-11-12。

来源：[AWS 与 Natera](https://aws.amazon.com/blogs/machine-learning/how-natera-designed-an-agentic-ai-system-for-lab-ops-with-amazon-bedrock-agentcore/)

## 9. Microsoft 委托 IDC 调查：企业 AI 回报仍集中于少数成熟组织

![调查中的成熟度与回报差异。调查范围：5,200+ 人 / 28 行业，IT 与业务负责人；平均 AI 回报：4 倍 vs 2.7 倍，成熟度最高 10% vs 慢速采用者；回报达到 5 倍：39% vs 4%，两组受访组织占比；衡量信心：93% vs 61%，成熟组 vs 整体组织](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/microsoft-idc-frontier-firms-study-2026-11-12.svg)

IDC 受访者自报数据；研究由 Microsoft 委托。

Microsoft 于 11 月 12 日发布其委托 IDC 完成的企业 AI 调查，覆盖 28 个行业、5200 多名 IT 和业务负责人。按 IDC 的 AI 成熟度划分，排名最高的 10%“Frontier Firms”报告平均 AI 回报为 4 倍，底部 30% 慢速采用者报告为 2.7 倍；39% 的前者称回报达到 5 倍以上，慢速采用者为 4%。

调查还显示，能够高度自信衡量 AI 业务价值的受访组织比例，在成熟组为 93%，整体组织为 61%。这些数字是受访者报告的结果，研究由 Microsoft 赞助，不能直接视为随机对照试验或各行业普遍可复现的投资回报。

分类：产业；状态：赞助调查结果；受访者自报；原文日期：2026-11-12。

来源：[Microsoft（委托 IDC）](https://blogs.microsoft.com/blog/2026/11/12/scaling-ai-value-without-losing-control-lessons-from-frontier-firms/)

## 10. IBM 体育科技创业挑战赛选出代理式 AI 公司 LivXP

![LivXP 获奖及后续支持。获奖者：LivXP，IBM 公布的挑战赛胜出者；最终入围：7 家初创公司，邀请制决赛阵容；概念验证支持：最高 $100,000，须另行审核及达成协议；IBM 技术额度：最高 $20,000，按赛事规则提供](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/ibm-livxp-sports-ai-prize-2026-11-12.svg)

最高额度须经过独立审核并签署协议。

IBM 于 11 月 12 日宣布，体育粉丝互动平台 LivXP 获得其 Web Summit Lisbon 体育科技创业挑战赛大奖。IBM 称，LivXP 提供连接球迷与球队、运动员及赛事体验的互动市场；本届邀请赛共有七家入围初创公司，挑战赛历时一年。

奖项包括最高 10 万美元的概念验证项目支持和最高 2 万美元 IBM 技术额度，但均须满足后续审查及协议条件。LivXP 对自身产品和全球覆盖范围的描述来自 IBM 新闻稿，目前公告没有披露具体合作项目的签约、上线时间或独立成效。

分类：产业；状态：创业挑战赛获奖；后续项目须另行审核；原文日期：2026-11-12。

来源：[IBM](https://newsroom.ibm.com/2026-11-12-ibm-announces-winner-of-sports-tech-startup-prize-challenge-at-web-summit-lisbon-2026)

## 11. SGLang-Neuron 通过 AWS 容器向 Trainium 用户开放

![SGLang-Neuron 开放路径。获得方式：AWS 深度学习容器，RadixArk 与 Annapurna Labs 合作；推理硬件：AWS Trainium，教程示例使用 Trainium3；调用方式：沿用 SGLang 接口，原生 PyTorch 执行路径；工作负载：推理与 RL rollout，支持范围以验证清单为准](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/aws-sglang-neuron-trainium-2026-11-12.svg)

上手示例与功能范围以 AWS 及项目文档为准。

AWS 于 11 月 12 日宣布，RadixArk 与 Annapurna Labs 合作开发的 SGLang-Neuron 已通过 AWS Deep Learning Container 公开提供。该插件让开发者在 AWS Trainium 上沿用 SGLang 的模型服务接口，用于推理服务及生成强化学习训练样本，底层使用原生 PyTorch 和 Trainium 专用组件。

AWS 的上手示例采用 Trainium3 实例和 gpt-oss-120b 模型，并说明插件还支持将提示词预处理与生成阶段拆分到不同服务器。官方文档提醒，实际支持的模型、功能和已验证配置以项目文档为准；公告没有提供独立性能对比。

分类：开源；状态：通过 AWS Deep Learning Container 公开提供；原文日期：2026-11-12。

来源：[AWS 与 RadixArk](https://aws.amazon.com/blogs/machine-learning/deploy-frontier-ai-models-on-aws-trainium-with-sglang-neuron/)

## 12. 澳洲研究团队用 DeepVariant 分析巨藻基因组

![从基因组分析到恢复研究。参考基因组：2 份，澳大利亚巨藻；野外样本：600 份 / 40 地点，塔斯马尼亚沿岸采集；遗传分析：DeepVariant，Google 开源变异分析工具；下一步目标：筛选耐热种群，用于后续生态恢复研究](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-kelp-deepvariant-australia-2026-11-12.svg)

研究结果与生态恢复目标须区分；数量为 Google 公布数据。

Google 于 11 月 12 日介绍与澳大利亚国家科学机构 CSIRO 合作的巨藻研究。团队公布两份澳洲巨藻参考基因组，并训练 Google 开源变异分析工具 DeepVariant 的一个版本分析塔斯马尼亚海岸 40 个地点采集的 600 份野生样本，以支持后续保护遗传学工作。

Google 的文章称，研究区域的巨藻数量已降至历史水平约 5%，团队希望结合基因分析和实验室杂交研究，筛选适应较暖海水的种群，为未来恢复工作打基础。此次公告描述的是研究进展和潜在路径，不表示已有大规模复种或生态恢复成效。

分类：研究；状态：基因组与样本分析进展；恢复仍属研究目标；原文日期：2026-11-12。

来源：[Google](https://blog.google/company-news/outreach-and-initiatives/sustainability/saving-giant-kelp-australia/)

## 13. Google Ads 增加无效流量支出透明度卡片

![无效流量账单信息展示。系统拦截：无效活动，Google 称后台会过滤；账户卡片：节省金额，新增展示支出避免额；事后识别：适用时抵扣，Google 对后续修正的说明；2026 年数据：平均降低 30%，Google 自报无效线索风险变化](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-ads-invalid-traffic-card-2026-11-12.svg)

界面功能与 30% 统计数字来自 Google 公告。

Google 于 11 月 12 日宣布在 Google Ads 推出 Invalid Traffic Overview Card，让广告主查看系统拦截的无效流量节省金额，以及事后识别后发放的抵扣。此前 Google 表示相关防护主要在后台运行；新卡片把部分处理结果展示在广告账户界面中。

Google 称，2026 年以来通过系统升级，广告主遭遇无效线索的平均风险下降 30%。该比例是 Google 对自身平台的统计，没有提供独立审计方法；公司还说明无效流量通常不会收费，事后发现时则在适用情况下抵扣。

分类：产品；状态：开始推出；效果数字为 Google 自报；原文日期：2026-11-12。

来源：[Google](https://blog.google/products/ads-commerce/invalid-traffic-overview-google-ads/)

## 14. Gemini Chrome 侧栏可在当前网页中提供问答

![网页旁的 Gemini 侧栏。打开：点击 Chrome 工具栏，在侧栏唤起 Gemini；总结：概括长报告，在当前网页旁查看；比较：核对商品信息，不必切换新标签；解释：改写为浅白语言，由 Gemini 生成说明](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-gemini-chrome-sidepanel-2026-11-12.svg)

功能操作来自 Google 文章；完整账户和地区条件未列明。

Google 于 11 月 12 日介绍 Chrome 中的 Gemini 侧栏功能：用户可从浏览器工具栏打开侧栏，在当前网页旁请求总结长报告、比较商品信息或用浅白语言解释内容，不必切换到新标签页。

这项功能将网页阅读与 Gemini 对话并排放置，Google 的说明重点在操作方式，没有披露完整的地区、账户和浏览器版本条件，也没有公布独立的网页总结准确率评估。敏感页面内容如何处理，应以用户当前账户可见的产品设置和隐私说明为准。

分类：产品；状态：官方功能说明；可用范围未详列；原文日期：2026-11-12。

来源：[Google](https://blog.google/innovation-and-ai/products/gemini-app/research-with-gemini-in-chrome/)

**历史归档**

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
