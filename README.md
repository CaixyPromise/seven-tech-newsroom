# Seven Tech Newsroom

每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。

[访问网站](https://caixypromise.github.io/seven-tech-newsroom/) · [RSS](https://caixypromise.github.io/seven-tech-newsroom/feed.xml) · [源码仓库](https://github.com/CaixyPromise/seven-tech-newsroom) · [作者主页](https://github.com/CaixyPromise) · [运行说明](OPERATIONS.md)

最近一期：2026-11-04。共 8 期、74 条独立记录；按实际发布状态与来源标时。

**最新数据快照**：2026-10-29 09:03 UTC+8；OpenRouter 日榜另截至 2026-10-31 UTC。

| 观察项 | 最新观测 | 范围 |
| --- | --- | --- |
| 模型基本费估算 | $0.002 · Claude Haiku 5.5 | 7 个选定模型，10K 输入 + 2K 输出 Token |
| 平台单日用量 | 约 7.09T Token · DeepSeek V4.1 Flash 1017 | OpenRouter 2026-10-31 UTC 公开日榜 |
| 开源关注 | 185,141 Stars · ollama/ollama | 本站固定跟踪的 6 个项目 |
| 文本模型下载 | 24,162,298 · Qwen/Qwen3-0.6B | HF 文本生成类，近 30 日滚动量 |

来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。

## 最新一期 · 2026-11-04

**AI 进入工程、教育与企业工作流**

本期整理 11 条经原始来源核实的 AI 与科技进展，涵盖教育产品、工程模型、开放模型、企业代理、安全治理与云业绩。

每日精选，第 008 期。收录范围：2026-11-03 09:00 至 2026-11-04 09:00（Asia/Singapore）；原文仅标日期者保留日期精度。。
实际首次整理：2026-11-04 09:06 UTC+8。
指标按实际保存的批次与采集时间查看。

## 1. Google 把 Guided Learning 扩展到 Classroom 与 Search

![AI 学习功能覆盖面。课堂：Guided Learning，扩展到 Google Classroom；搜索：学习引导能力，带入 Google Search；学生控制：K-12 账号，更新多项 AI 服务设置](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-ai-learning-era-2026-11-03.svg)

Google 对产品更新的公告；各产品开放情况可能不同。

Google 11 月 3 日公布一组面向教育场景的 AI 更新：Guided Learning 将在全球 Google Classroom 推出，Google Search 也会加入相关引导式学习能力。公司同时调整 Gemini、NotebookLM、Classroom 和 Search 的 K-12 学生账号控制。

公告还包括新研究、Google.org 资助和教师 AI 培训扩展。Google 将这些变化定位为教育产品更新；具体功能在各服务中的开放时间与地区范围，需以产品界面和学校管理员设置为准。

分类：产品；状态：产品更新；各服务开放范围不同；原文日期：2026-11-03。

来源：[Google](https://blog.google/products-and-platforms/products/education/ai-learning-era-2026/)

## 2. OpenAI 展示模型辅助机械与电子工程的试验

![模型进入工程工作流。设计：CAD 与 PCB，探索机械、电气设计；验证：仿真与审查，工程师检查模型结果；合作：Mazda / CGR，评估真实工程任务](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/openai-physical-engineering-2026-11-03.svg)

厂商展示的内部与合作试验，仍需工程师检查。

OpenAI 11 月 3 日介绍其模型在机械与电子工程中的试验，包括生成 CAD 设计、PCB 方案、制造图纸、设置模拟和协助设计审查。公司称其硬件团队自 2 月以来的模型使用量按 token 计算增长 23 倍，这是内部使用数据。

公告同时披露与 Chip Ganassi Racing 的合作及新加入的 Mazda 研究合作，工程师会审查模型产出。OpenAI 也指出原型仍需多轮检查，当前重点是受控协作和评估，还不是面向所有工程团队的普遍产品承诺。

分类：研究；状态：合作试验；尚非普遍产品；原文日期：2026-11-03。

来源：[OpenAI](https://openai.com/index/accelerating-engineering-for-the-physical-world/)

## 3. Sarvam 发布开放权重决策模型 Prism

![面向选项判断的模型。基础模型：Sarvam 105B，LoRA 微调的决策模型；综合得分：71.8，厂商三项指数平均；中位响应：44 ms，B200 单请求测试](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/sarvam-prism-decision-model-2026-11-03.svg)

三项指数与延迟为 Sarvam 自行测试结果。

Sarvam 11 月 3 日发布 Sarvam Prism，一个针对给定状态、问题与候选项输出概率的决策模型，采用 Sarvam 105B 的 LoRA 微调。公司称模型权重以 Apache 2.0 许可开放，推理需要至少 120 GB 显存；另提供 Sarvam API 接入。

在 Sarvam 自行运行的 25 个决策模型比较中，Prism 三项指数平均得分为 71.8，中位响应时间为 44 毫秒，测试使用 B200 GPU。上述是厂商披露的评测结果，指标组合包含内部印度语言基准，不等同于独立通用评测。

分类：模型；状态：开放权重；评测为厂商自测；原文日期：2026-11-03。

来源：[Sarvam AI](https://www.sarvam.ai/blogs/sarvam-prism)

## 4. Open WebUI 0.13.0 加入标签式工作区

![聊天界面扩展为工作区。工作区：多标签，文件、终端、预览等；协作：MCP Apps，支持侧边聊天；升级提示：不支持滚动升级，含数据库 schema 变更](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/open-webui-v013-release-2026-11-03.svg)

升级前须处理数据库变更；不支持滚动升级。

Open WebUI 在 GitHub 于 11 月 3 日发布 0.13.0。更新加入标签式工作区，可在同一聊天中切换文件、多个终端、产物、预览、语音通话和评论，也可拖动标签排序并将文件保存到选定终端。

版本说明还列出聊天中的 MCP Apps、侧边聊天，以及单次响应工具调用轮数上限提升至 1,024。升级时需留意该版本包含数据库 schema 变更，项目说明滚动升级不受支持；部署方应按发布说明安排更新。

分类：开源；状态：正式发布；升级需安排；原文日期：2026-11-03。

来源：[GitHub · open-webui](https://github.com/open-webui/open-webui/releases/tag/v0.13.0)

## 5. CrowdStrike 推出 AI Kill Switch，先从网关切断代理

![失控代理的人工制动。触发方：授权管理员，保留操作审计记录；当前控制点：AI Gateway，先切断模型访问；后续扩展：端点进程，CrowdStrike 称即将支持](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/crowdstrike-ai-kill-switch-2026-11-03.svg)

网关阻断已推出；端点直接终止仍在后续计划中。

CrowdStrike 11 月 3 日宣布 Falcon Guardian 的 AI Kill Switch 可用。公司说明，授权管理员可在代理出现偏离行为时，从网关侧终止其模型访问、阻止再次启动并切断企业网络连接，操作会留下审计记录。

当前终止能力先在 Gateway 执行；直接在端点终止代理进程仍属后续扩展。该功能面向 Falcon Guardian 客户，公告同时介绍的其他端点和代理控制能力有不同发布阶段，不能一概视为已上线。

分类：治理；状态：Falcon Guardian 客户可用；原文日期：2026-11-03。

来源：[CrowdStrike](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-introduces-ai-kill-switch-for-ai-safety/)

## 6. Scite 与 Article Galaxy 接入 Microsoft Copilot

![从研究证据到使用许可。证据核验：Scite，支持、反驳或提及引用；全文获取：Article Galaxy，查看订阅与价格；许可核对：按文章判断，包括生成式 AI 使用权](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/research-solutions-copilot-research-2026-11-03.svg)

集成已上架；全文和 AI 使用权取决于订阅与许可。

Research Solutions 11 月 3 日宣布 Scite 和 Article Galaxy 集成到 Microsoft Copilot。Scite 的 Smart Citations 会标注后续研究对论文结论的支持、反驳或提及；Article Galaxy 则查询机构订阅、获取价格及单篇文章的使用权。

该组合允许用户在 Microsoft 365 工作流中查找证据，并核对全文能否用于特定场景，包括生成式 AI 和文本数据挖掘。公司称两项集成已在 Microsoft Marketplace 上架；实际可访问内容与许可仍取决于机构订阅和文章授权。

分类：产品；状态：Microsoft Marketplace 已上架；原文日期：2026-11-03。

来源：[Research Solutions](https://www.researchsolutions.com/resources/press-releases/research-solutions-brings-scite-and-article-galaxy-to-microsoft-copilot)

## 7. Snowflake 扩展 CoCo 与 CoWork 的后台代理功能

![企业代理更新与开放阶段。后台任务：Bots，即将进入私有预览；自动化：重复工作流，部分能力已 GA；应用入口：Slack / Sheets，多项处于公开预览；路由：模型分级，私有预览](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/snowflake-coco-cowork-bots-2026-11-03.svg)

Snowflake 标注的 GA、公开预览、私有预览与即将预览。

Snowflake 11 月 3 日公布 CoCo 与 CoWork 的一组更新，覆盖后台 Bots、重复任务自动化、记忆与技能共享，以及 Slack、Excel、Sheets 和移动端入口。公司称新 Bots 会在授权和角色边界内执行工作，并在需要决策或批准时回到用户。

发布说明将不同功能标为不同阶段：部分自动化已 GA，多项应用和资料功能为公开预览，动态模型路由为私有预览，Bots 仍标注“即将进入私有预览”。截至 2026 年 7 月季度末，公司报告 CoWork 使用账户超过 5,800、CoCo 超过 9,100；这是厂商口径。

分类：产品；状态：分阶段发布；原文日期：2026-11-03。

来源：[Snowflake](https://www.snowflake.com/en/news/press-releases/expedition-2026-coco-cowork/)

## 8. 6sense 推出面向销售团队的 Agentic GTM 更新

![销售代理功能分阶段推出。现已可用：Sales MCP，兼容代理查询销售情报；11 月 Beta：BDR / Explainability，尚未普遍开放；12 月 Beta：AI Visibility，计划监测品牌 AI 曝光；2027 年 2 月：完整可解释性，厂商公布的目标时间](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/6sense-agentic-gtm-products-2026-11-03.svg)

按 6sense 公告区分正式可用、Beta 与未来计划。

6sense 在 11 月 3 日的 Breakthrough 2026 活动上宣布一组面向销售流程的产品更新，包括 BDR Agent、AI Visibility、预测模型和销售情报 MCP。公司称销售情报 MCP 当日一般可用，关键字意图 API 纳入正式版本。

其他功能的开放进度不同：BDR Agent 与可解释性功能计划 11 月 Beta，AI Visibility 预计 12 月 Beta，预测模型先进入封闭 Beta，完整可用安排延至 2027 年 2 月。公告中的买家调研数字来自 6sense 自身研究。

分类：产品；状态：部分 GA；多数功能为 Beta 或计划；原文日期：2026-11-03。

来源：[6sense](https://6sense.com/news/6sense-repositions-as-partner-for-agentic-gtm-unveils-new-brand-and-major-product-innovations-at-breakthrough-2026)

## 9. DataCore 为 SANsymphony 上线存储运维 AI 助手

![存储运维问答的产品范围。当前产品：SANsymphony，10.0 PSP21 及以上；输入信息：遥测 + 文档，查询存储运行状态；后续范围：Swarm，对象存储支持待推出](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/datacore-ai-sansymphony-2026-11-03.svg)

当前支持 SANsymphony；Swarm 尚属后续计划。

DataCore 11 月 3 日发布 DataCore AI，面向其 SANsymphony 软件定义存储平台提供自然语言运维助手。公告称该助手结合运行遥测、产品文档和厂商经验，支持管理员查询存储池、虚拟磁盘延迟和数据保护配置等状态。

目前可用范围为 SANsymphony 10.0 PSP21 及以上版本；对象存储产品 Swarm 的支持列为后续计划。DataCore 没有在公告中提供独立验证的故障处理提速或准确率数据，决策仍由管理员负责。

分类：产品；状态：已发布；限定 SANsymphony 版本；原文日期：2026-11-03。

来源：[DataCore](https://www.datacore.com/news-post/datacore-launches-ai-assistant-that-turns-storage-questions-into-expert-answers/)

## 10. Protegrity 用 Cedar 统一企业 AI 访问策略

![策略覆盖企业 AI 三层。数据：访问策略，保护敏感业务上下文；代理：Cedar 引擎，统一策略控制基础；推理：AI Gateway，纳入策略执行范围；技术预览：Secure Query，与 Iceberg Protector 同阶段](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/protegrity-ai-team-policy-engine-2026-11-03.svg)

厂商公布的产品能力；部分组件处于技术预览。

Protegrity 11 月 3 日宣布 AI Team Edition 更新，新增基于开源 Cedar 策略语言的策略引擎，目标是在数据访问、代理执行和模型推理层统一应用企业规则，并与其 PII 模型集成。

公司还列出 AI Gateway、Data & AI Fast Lanes 等组件，以及处于技术预览阶段的 Secure Query 和 Iceberg Protector。公告描述的是厂商产品能力，没有披露独立评测或客户规模数据；可用阶段需按各组件分别确认。

分类：治理；状态：产品更新；部分功能预览；原文日期：2026-11-03。

来源：[Protegrity](https://www.protegrity.com/news/protegrity-brings-secure-context-to-enterprise-ai-with-a-unified-policy-engine-for-data-agents-and-inference)

## 11. DigitalOcean 三季度 AI 客户 ARR 达 3.76 亿美元

![AI 客户收入与季度表现。第三季度营收：$321M，同比增长 40%；AI 客户 ARR：$376M，同比增长 288%；季度新增 ARR：$160M，公司披露的季度纪录](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/digitalocean-q3-ai-arr-2026-11-03.svg)

ARR 为公司将最近季度对应收入乘以四的年化指标。

DigitalOcean 11 月 3 日公布截至 9 月 30 日的第三季度业绩，营收为 3.21 亿美元、同比增长 40%。公司披露 AI 客户年度经常性收入（ARR）为 3.76 亿美元，同比增长 288%，季度新增 ARR 达 1.6 亿美元。

公司同时将第四季度收入增长展望上调至 44%—45%，并预计 2027 年收入增长超过 60%。DigitalOcean 定义 AI 客户 ARR 为最近季度 AI 客户收入乘以四；这是公司自定的年化指标，不能直接等同于季度现金收入或全行业市场规模。

分类：产业；状态：三季度财报；ARR 为年化口径；原文日期：2026-11-03。

来源：[DigitalOcean](https://investors.digitalocean.com/news/news-details/2026/DigitalOcean-Announces-Third-Quarter-2026-Financial-Results/default.aspx)

**历史归档**

- [2026-11-04 · AI 进入工程、教育与企业工作流](archive/2026-11-04.md)
- [2026-11-03 · 模型、算力基础设施与企业 AI 应用继续推进](archive/2026-11-03.md)
- [2026-11-01 · 开放模型、智能体与安全机制迎来新进展](archive/2026-11-01.md)
- [2026-10-29 · 前沿模型、智能体工具与企业部署继续扩展](archive/2026-10-29.md)
- [2026-10-28 · 模型研究、企业代理与 AI 基础设施的多线推进](archive/2026-10-28.md)
- [2026-10-27 · 企业 AI 加入流程与数据层，终端和资本市场出现新动作](archive/2026-10-27.md)
- [2026-10-26 · AI 正在进入工具、数据与日常工作](archive/2026-10-26.md)
- [2026-10-23 · 模型能力向前一步，工具与证据也要跟上](archive/2026-10-23.md)
