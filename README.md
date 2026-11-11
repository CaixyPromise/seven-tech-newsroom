# Seven Tech Newsroom

每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。

[访问网站](https://caixypromise.github.io/seven-tech-newsroom/) · [RSS](https://caixypromise.github.io/seven-tech-newsroom/feed.xml) · [源码仓库](https://github.com/CaixyPromise/seven-tech-newsroom) · [作者主页](https://github.com/CaixyPromise) · [运行说明](OPERATIONS.md)

最近一期：2026-11-11。共 15 期、130 条独立记录；按实际发布状态与来源标时。

**最新数据快照**：2026-11-11 11:50 UTC+8；OpenRouter 日榜另截至 2026-10-31 UTC。

| 观察项 | 最新观测 | 范围 |
| --- | --- | --- |
| 模型基本费估算 | $0.00106 · DeepSeek V4.1 Flash 1017 | 7 个选定模型，10K 输入 + 2K 输出 Token |
| 平台单日用量 | 约 7.09T Token · DeepSeek V4.1 Flash 1017 | OpenRouter 2026-10-31 UTC 公开日榜 |
| 开源关注 | 186,591 Stars · ollama/ollama | 本站固定跟踪的 6 个项目 |
| 文本模型下载 | 32,217,183 · openai-community/gpt2 | HF 文本生成类，近 30 日滚动量 |

来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。

## 最新一期 · 2026-11-11

**前沿模型、企业智能体与 AI 芯片更新**

Google 发布 Gemini 4 Carbon，Anthropic 扩展企业协作工具；芯片、医疗服务与产业投资也有新进展。

每日精选，第 015 期。收录范围：2026-11-10 09:00 至 2026-11-11 09:00（Asia/Singapore）；按原始来源时间核实，日期精度来源未推断具体时分；收录 13 条独立消息。
实际首次整理：2026-11-11 11:50 UTC+8。
指标按实际保存的批次与采集时间查看。

## 1. Google 发布 Gemini 4 Carbon，API 与企业版开放

![模型开放范围与 API 价格。输入价格：$2 / 百万 Token，Google 公布的 API 定价；输出价格：$10 / 百万 Token，Google 公布的 API 定价；企业与开发者：API / Business，官方公告称已开放使用；并行协作：/swarm 预览，随模型发布提供的预览功能](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-gemini-4-carbon-2026-11-11.svg)

价格与开放状态据 Google 公告；/swarm 仍为预览。

Google 于 11 月 10 日发布 Gemini 4 Carbon，面向开发者和企业客户开放 API 与 Gemini for Business 使用；Google AI Ultra 消费者将按地区逐步获得访问权限。Google 同时推出名为 /swarm 的并行协作功能预览。

官方列出的 API 价格为每百万输入 Token 2 美元、每百万输出 Token 10 美元。Google 将 Carbon 定位为适合复杂推理与长任务的模型，相关能力描述和性能数据来自厂商发布材料，实际效果仍需结合具体任务评估。

分类：模型；状态：API 与 Business 可用；消费者分批开放；/swarm 预览；原文日期：2026-11-10T16:00:00+00:00。

来源：[Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)

## 2. OpenAI 推出 ChatGPT 商家资料与商品信息入口

![商家信息进入 ChatGPT 的路径。商家入口：认领资料，企业核验并维护信息；商品发现：提交产品目录，供 ChatGPT 展示商品与服务；互动反馈：聚合提及与点击，部分指标设有隐私门槛；商业代理：美国部分企业，电商与线上服务，需符合条件](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/openai-businesses-chatgpt-2026-11-11.svg)

产品目录与商业代理的开放范围不同；代理目前限美国部分企业。

OpenAI 于 11 月 10 日推出 Businesses in ChatGPT，让符合条件的商家认领企业资料、核验信息并提交产品目录，以便用户在 ChatGPT 中发现商品和服务。商家还可查看聚合后的提及和点击数据；部分指标会受隐私门槛限制。

OpenAI 另开放商业代理，目前仅面向符合条件的美国电商和线上服务企业。商家入口、目录展示和代理功能处于不同可用阶段，不能把信息展示等同于订单转化；现阶段公布的指标主要反映平台内互动。

分类：产品；状态：商家资料与目录入口推出；商业代理目前限符合条件的美国企业使用；原文日期：2026-11-10。

来源：[OpenAI](https://openai.com/index/introducing-businesses-chatgpt/)
来源：[TechCrunch](https://techcrunch.com/2026/11/10/openai-rolls-out-new-business-profiles-making-chatgpt-just-a-little-bit-more-like-google/)

更正：2026-11-11T03:51:58+00:00 · 将商业代理概述明确为已向符合条件的美国电商和线上服务企业开放，避免表述为试点。

## 3. Anthropic 为 Claude 增加白板与表格协作工具

![三项协作工具的开放阶段。Whiteboards：测试版，付费计划可用，企业默认关闭；Sheets：测试版，可配合数据连接器使用；Claude Data：正式可用，企业版计划 11 月 19 日启用](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/anthropic-claude-workspace-tools-2026-11-11.svg)

官方公告区分测试版、正式可用及企业默认设置。

Anthropic 11 月 10 日公布 Claude Whiteboards 和 Claude Sheets，作为面向付费计划用户的测试版协作工具；原 Claude Dashboards 更名为 Claude Data，并转为正式可用。相关功能可在网页、桌面和移动端使用。

Anthropic 的同日公告还介绍互动连接器升级，允许用户在 Claude 会话旁或全屏打开 Adobe、Atlassian、Box 等伙伴应用。企业版默认设置有所不同：Whiteboards 与 Sheets 默认关闭，Claude Data 则将在 11 月 19 日启用。

分类：产品；状态：Whiteboards / Sheets 测试版；Claude Data 正式可用；原文日期：2026-11-10。

来源：[Anthropic](https://claude.com/resources/articles/sheets-whiteboards-data)
来源：[Anthropic](https://claude.com/resources/articles/more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors)

更正：2026-11-11T03:58:14+00:00 · 区分 Claude 内的白板/表格工具与同日发布的互动连接器，避免把两类功能混写。

## 4. Adobe MAX 扩展创意 AI 工具并加入 MCP 集成

![创意 AI 更新覆盖的产品层。内容生成：Firefly，创意生成与代理工具更新；专业创作：四款桌面应用，加入本地 MCP 集成方案；营销工作流：GenStudio，面向营销创意工作的更新；开放状态：预览 / 私测 / 已开放，需逐项查看 Adobe 的可用说明](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/adobe-max-creative-ai-2026-11-11.svg)

Adobe 公布多项更新；各功能的开放阶段有所不同。

Adobe 于 11 月 10 日在 MAX 公布面向 Firefly、Creative Cloud 和 GenStudio 的多项 AI 更新，并为 Photoshop、Illustrator、Premiere 和 After Effects 增加本地 MCP 集成方案。公司还宣布与 Google、Microsoft、OpenAI、Anthropic 等厂商开展创意工具合作。

发布内容包括已开放、预览和私测项目，具体状态因功能而异；Adobe 的公告没有把所有更新列为普遍可用。Adobe 另宣布与 Disney 达成多年期创意 AI 合作，授权范围和可用功能应按各自产品公告理解。

分类：产品；状态：多项产品更新已公布；部分仍属预览或私测；原文日期：2026-11-10。

来源：[Adobe](https://news.adobe.com/news/2026/11/adobe-powers-new-era-of-creativity)
来源：[TechCrunch](https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/)

## 5. IBM 与 Microsoft 推出面向行业的智能体平台

![Imagine Enterprise 的平台构成。IBM 资产：6,000+，预置智能体及相关资产；技术底座：Microsoft 云与 AI，并提供安全基础设施；首批行业：金融 / 保险 / 零售，初始行业框架；交付方式：顾问服务或自管，IBM Consulting 参与交付](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/ibm-microsoft-imagine-enterprise-2026-11-11.svg)

6,000 多项预置资产为 IBM 的披露；公告尚未给出部署成效。

IBM 与 Microsoft 于 11 月 10 日宣布 Imagine Enterprise，面向金融、保险和零售等行业构建 AI 智能体平台。IBM 称将带来 6,000 多个预置智能体和相关资产，Microsoft 提供云、AI 与安全基础设施。

平台计划通过 IBM Consulting 交付，并为客户提供自主管理选项。双方把它定位为行业转型方案，当前公告描述的是平台发布和合作安排，尚不能据此判断各行业客户的部署结果。

分类：产业；状态：平台与合作已宣布；初始行业框架包括金融、保险和零售；原文日期：2026-11-10。

来源：[IBM](https://newsroom.ibm.com/2026-11-10-ibm-and-microsoft-announce-a-new-ai-agent-platform-designed-for-industry-specific-transformation)

## 6. Anthropic 向 SEC 更新 IPO 发行价格区间

![S-1/A 列出的拟议发行条款。拟议价格：$70–78 / 股，注册文件所列价格区间；新发股份：801,351,354 股，由 Anthropic 发行；股东出售：23,648,646 股，由现有股东出售；上市代码：ANT，拟在纳斯达克上市，待注册生效](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/anthropic-ipo-s1a-terms-2026-11-11.svg)

价格和股份数来自 SEC 文件；注册声明尚未生效。

Anthropic 于 11 月 10 日向美国证券交易委员会提交 S-1/A 注册文件，为拟议 IPO 列出每股 70 至 78 美元的价格区间。文件显示，公司拟发行 801,351,354 股 A 类普通股，现有股东另拟出售 23,648,646 股。

该次发行合计 8.25 亿股，计划在纳斯达克以 ANT 代码上市；SEC 文件同时注明注册声明尚未生效。上述是申报文件中的拟议条款，价格、发行规模和上市安排仍可能在正式生效前调整。

分类：产业；状态：S-1/A 已提交；拟议发行尚待注册生效；原文日期：2026-11-10T06:29:24-05:00。

来源：[美国证券交易委员会（SEC）](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)
来源：[美国证券交易委员会（SEC）](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/0001628280-26-072484-index.htm)

## 7. AMD 发布第六代 EPYC 服务器处理器

![处理器出货与云实例进度。处理器：Zen 6 / SP7，第六代 EPYC 服务器平台；OEM / ODM：系统已出货，AMD 称合作伙伴已开始发货；Azure / OCI：预计稍后推出，云实例仍属后续计划](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/amd-epyc-6th-gen-2026-11-11.svg)

已出货系统与后续云实例据 AMD 公告区分。

AMD 于 11 月 10 日发布第六代 EPYC 服务器处理器，采用 Zen 6 架构和 SP7 平台。AMD 表示，OEM 与 ODM 合作伙伴的系统已经开始出货，Azure 和 OCI 云实例则预计稍后推出。

AMD 将新处理器定位于通用服务、GPU 主机节点及智能体沙箱等工作负载，并公布自有基准测试结果。现阶段可购买的是合作伙伴系统；云实例仍处于后续计划，性能数字应按 AMD 的测试配置和口径理解。

分类：基础设施；状态：OEM / ODM 系统已开始出货；Azure 与 OCI 云实例待推出；原文日期：2026-11-10T15:39:50+00:00。

来源：[AMD](https://newsroom.amd.com/news/6th-gen-epyc-lead-ai-enterprise-computing/)

## 8. NVIDIA 发布面向自动驾驶推理的 Alpamayo 2 Edge

![模型发布与硬件验证范围。模型规模：约 2B 参数，驾驶视觉语言动作模型；权重 / 代码：OpenMDW-1.1 / Apache-2.0，按模型卡所列许可；已验证 GPU：H100 80GB，其他 GPU 配置尚未验证；显存建议：至少 16GB，模型卡提供的硬件建议](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/nvidia-alpamayo-2-edge-2026-11-11.svg)

参数与许可据模型卡；只有 H100 80GB 配置列为已验证。

NVIDIA 于 11 月 10 日发布 Alpamayo 2 Edge，定位为面向自动驾驶场景的 20 亿参数级视觉语言动作模型，加入自适应推理能力并开放模型权重。NVIDIA 将其面向 DRIVE AGX Thor 等车载计算平台的开发工作。

模型卡标注权重采用 OpenMDW-1.1 许可，代码使用 Apache-2.0；目前只有 H100 80GB 配置经过验证，文档建议至少 16GB 显存。发布材料描述的是模型与开发支持，尚不能据此推断车辆级产品已完成道路或安全认证。

分类：开源；状态：权重与代码已发布；硬件验证范围有限；原文日期：2026-11-10T16:00:00+00:00。

来源：[NVIDIA 开发者博客](https://developer.nvidia.com/blog/running-av-reasoning-models-within-onboard-compute-and-latency-limits/)
来源：[NVIDIA / Hugging Face](https://huggingface.co/nvidia/Alpamayo2-Edge)

## 9. Arm 推出面向边缘 AI 的 Cortex-M42 处理器 IP

![边缘 AI 微控制器 IP 的变化。向量计算：最高 3 倍，Arm 对比 Cortex-M33；向量能效：最高 2 倍，Arm 公布的相对提升；扩展能力：ML / DSP / Helium，面向微控制器级边缘设备；产品阶段：处理器 IP，供芯片设计方授权使用](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/arm-cortex-m42-2026-11-11.svg)

性能对比是 Arm 相对 Cortex-M33 的官方数据。

Arm 于 11 月 10 日发布 Cortex-M42 处理器 IP，面向边缘 AI 与嵌入式设备，集成机器学习和 DSP 能力，并支持 Helium 向量扩展。Arm 称，相较 Cortex-M33，其向量计算能力最高提升 3 倍、向量能效最高提升 2 倍。

这些比较数据由 Arm 提供，实际效果取决于工作负载和芯片实现。Cortex-M42 是授权给芯片设计方的处理器 IP，公告代表产品设计可用，不代表搭载该 IP 的终端芯片已经量产上市。

分类：基础设施；状态：处理器 IP 已发布并开放给芯片设计方授权；原文日期：2026-11-10T14:00:00+00:00。

来源：[Arm](https://newsroom.arm.com/news/arm-cortex-m42-accelerate-edge-ai-innovation)

## 10. Oura 拟以 6.25 亿美元收购 Counsel Health

![拟议收购金额与交割安排。交易金额：$625M 现金，金额可能按协议调整；交易状态：收购协议已签署，交割尚未完成；预计时间：2026 年底前，仍需满足惯常交割条件](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/oura-counsel-health-acquisition-2026-11-11.svg)

交易金额及预计时间来自公司公告，交割仍待惯常条件。

Oura 于 11 月 10 日宣布，将以 6.25 亿美元现金收购 AI 原生初级医疗服务公司 Counsel Health，交易仍需完成惯常交割条件。公司预计在年底前完成收购，金额可能按协议作调整。

Oura 将这笔交易描述为把可穿戴健康数据与医疗服务相连接的计划，Counsel Health 的服务由 AI 工具和医生共同支持。公告说明的是拟议收购及业务方向，交易尚未交割，不能视为 Oura 医疗服务已全面上线。

分类：产业；状态：收购协议已签署；预计年底前交割，仍待惯常条件满足；原文日期：2026-11-10。

来源：[Counsel Health](https://www.counselhealth.com/newsroom/oura-to-acquire-counsel-health-advancing-vision-for-more-connected-personalized-healthcare)
来源：[TechCrunch](https://techcrunch.com/2026/11/10/oura-to-acquire-ai-native-primary-care-startup-counsel-health-for-625m/)

## 11. Proximal Ventures 完成 2750 万美元首期基金募集

![首期基金规模与投资范围。基金规模：$27.5M，超过最初 25M 美元目标；单笔投资：$0.5M–$1.5M，管理方公布的计划范围；投资阶段：Pre-seed / Seed，生命科学 AI 早期项目；已支持项目：6 家初创公司，管理方披露的现有投资组合](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/proximal-ventures-life-science-fund-2026-11-11.svg)

基金募集和已投数量据管理方；不代表项目临床结果。

专注生命科学 AI 的 Proximal Ventures 于 11 月 10 日宣布完成 2,750 万美元首期基金募集，高于最初 2,500 万美元目标。基金计划投资种子前和种子轮项目，单笔支票预计为 50 万至 150 万美元。

管理方称该基金已支持六家初创公司，重点覆盖将 AI 用于药物研发和生命科学基础设施的团队。基金规模、投资策略和已投数量均为管理方披露；它们反映的是投资计划与募资进展，并不代表相关药物研发项目已取得临床结果。

分类：产业；状态：首期基金募集完成，进入早期项目投资阶段；原文日期：2026-11-10。

来源：[Proximal Ventures（新闻稿转载）](https://www.tmcnet.com/usubmit/-proximal-ventures-announces-275-million-debut-fund-invest-/2026/11/10/10479050.htm)
来源：[TechCrunch](https://techcrunch.com/2026/11/10/proximal-ventures-raises-debut-fund-to-back-startups-bringing-ai-to-drug-development/)
来源：[Proximal Ventures](https://proximal.vc/)

## 12. Synopsys 与 Infineon 推出 AURIX RC1 虚拟开发套件

![从虚拟平台到实体硬件验证。目标芯片：AURIX TC4x RC1，Infineon 微控制器系列；提前开发：虚拟平台，芯片到货前编写并测试软件；厂商估计：最高 90%，软件验证可在实体系统前完成；最终阶段：目标硬件验证，虚拟平台不能替代真实芯片](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/synopsys-infineon-aurix-vdk-2026-11-11.svg)

最高 90% 为 Synopsys 的工具能力估计，最终仍需真机验证。

Synopsys 于 11 月 10 日发布面向 Infineon AURIX TC4x RC1 微控制器系列的虚拟开发套件，让汽车和物理 AI 团队可在实际芯片到货前开发与测试软件。套件通过虚拟平台模拟微控制器环境及相关软件行为。

Synopsys 称，这种方式可在实体系统具备之前完成最高 90% 的软件验证；该数字是厂商对其工具的估计，取决于验证范围与项目配置。虚拟开发套件现阶段支持提前开发，不能替代真实芯片和目标硬件上的最终验证。

分类：基础设施；状态：虚拟开发套件已公布；支持芯片到货前的软件开发；原文日期：2026-11-10。

来源：[Synopsys](https://news.synopsys.com/2026-11-10-Synopsys-Advances-Virtual-Development-of-Next-Generation-Automotive-and-Physical-AI-Applications-with-Infineon-AURIX-TM-RC1-Microcontroller-Family)

## 13. IBM Impact Accelerator 选出四家教育与就业合作机构

![教育与未来工作合作计划。新一轮伙伴：4 家组织，教育与未来工作主题；支持内容：技术 + 专业协助，未逐项公布各机构金额；全项目投入：最高 $75M，现金与实物支持，截至 2028 年](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/ibm-impact-accelerator-learning-work-2026-11-11.svg)

7,500 万美元为整个项目到 2028 年的支持上限。

IBM 于 11 月 10 日公布 Impact Accelerator 教育与未来工作主题的四家合作组织，将提供技术资源和专业支持，协助推进教育及劳动力发展项目。IBM 称，该项目组合使用 AI、量子计算等技术方向。

公司披露的 7,500 万美元是整个 Accelerator 项目截至 2028 年的现金与实物支持上限，并非本期四家机构各自获得的金额。此次公告列出新一轮合作伙伴，尚未公布各项目对应的单独预算与量化成果。

分类：产业；状态：四家合作组织已选出；具体项目预算未逐项公布；原文日期：2026-11-10。

来源：[IBM](https://newsroom.ibm.com/2026-11-10-ibm-impact-accelerator-brings-ai-and-quantum-to-the-future-of-learning-and-work)

**历史归档**

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
