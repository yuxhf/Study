# [15] Insecure Coding Preferences in Long-Term Memory: Security Risks for LLM-based Code Generation：定向核验笔记

核验日期：2026-11-17。用途：研究辅助，不是课程综述正文。

## 身份与来源

- paper_id：doi:10.1145/3832170
- 正式出处：ISSTA 2026 Research Papers / PACMSE；卷期文章号仍待出版社核实。
- [正式记录](https://conf.researchr.org/details/issta-2026/issta-2026-research-papers/79/Insecure-Coding-Preferences-in-Long-Term-Memory-Security-Risks-for-LLM-based-Code-Ge)；[本次阅读来源](https://arxiv.org/abs/2607.17619)。
- 本次进度：全文已取得，定向阅读方法、关键实验及局限；未完成所有附录逐项核查或独立复现实验。PDF/text位于同级sources/paper_15.pdf、paper_15.txt。

## 研究定位

- 问题：长期保存的不安全编码偏好是否持续影响后续生成的安全性？
- 意义：把供应链风险从训练数据扩展到推理期长期记忆这一输入依赖。
- 方法：对记忆开/关进行配对测试，以功能及安全单元测试和人工警告标注评估；采用100个SALLM Python任务和94个CWEval非Python任务，每任务3次生成。
- 已核数值：Table1（PDF p.9）：Python跨k=1,2,3的平均Vul@k，ChatGPT 59.5%→73.3%，Gemini 62.7%→74.0%；不是单次Vul@1，100个Python任务每条件300份输出。
- 边界：正式会议摘要是两模型；可访问作者稿扩展四模型五语言，必须分版本；高风险预选条目上的100%过滤不能外推。

## 版本冲突与补充实验

- 正式会议页面摘要只列ChatGPT、Gemini；风险提升11.3–13.8（官网用百分号，可访问全文用百分点），未列Qwen、Grok及记忆过滤实验。
- 可访问arXiv PDF §5.2（p.6）列GPT-4o、Gemini-2.5 Flash、Qwen-3.5-Plus、Grok-4.2，前两者2025-07-01至08-06测试，后两者2026-03-24至05-15测试；作者稿表格不能未经确认就视为出版社最终实验。
- 作者稿Table7（pp.17–18）过滤实验仅用29个ChatGPT、28个Gemini的预选问题对应记忆，所选任务原本无记忆时均不出现安全测试失败。GPT-4o/Gemini过滤器均检测100%；对应平均时间1.53/2.90秒；这不是开放分布误报率、召回率验证。
- 同表：ChatGPT提示追加安全要求使平均Pass@k 77.8%→61.9%（下降15.9个百分点），平均Vul@k 53.4%→29.0%；这是预选子集结果。
- 作者局限（§8，p.20附近，以PDF页标为准）：服务随机性、人工标注、提示模板敏感性、脚本实现。研究者补充：缺少干净/模糊记忆混合测试时不能证明过滤误报足够低。

## Word摘要卡

- 研究问题：长期保存的不安全编码偏好是否持续影响后续生成的安全性？
- 意义：把供应链风险从训练数据扩展到推理期长期记忆这一输入依赖。
- 方法：对记忆开/关进行配对测试，以功能及安全单元测试和人工警告标注评估；采用100个SALLM Python任务和94个CWEval非Python任务，每任务3次生成。
- 实验与页码：Table1（PDF p.9）：Python跨k=1,2,3的平均Vul@k，ChatGPT 59.5%→73.3%，Gemini 62.7%→74.0%；不是单次Vul@1，100个Python任务每条件300份输出。
- 局限：正式会议摘要是两模型；可访问作者稿扩展四模型五语言，必须分版本；高风险预选条目上的100%过滤不能外推。
- 作者写作任务：解释记忆污染与模型权重后门的差异，并用功能/安全双指标评估过滤收益。
