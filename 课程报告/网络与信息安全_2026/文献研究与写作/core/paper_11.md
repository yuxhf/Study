# [11] Beyond Functional Correctness: Exploring Hallucinations in LLM-Generated Code

paper_id: doi:10.1109/TSE.2026.3657432。Fang Liu, Yang Liu, Lin Shi, Zhen Yang, Li Zhang, Xiaoli Lian, Zhongqi Li, Yuchi Ma；IEEE TSE52(3):1037–1055 (2026)。[正式页](https://ieeexplore.ieee.org/document/11361549)；[arXiv:2404.00971](https://arxiv.org/abs/2404.00971)。本地最新作者稿21页，与正式排版页码不同，以下为本地PDF顺序。2026-11-17定向全文核验分类、样本、列联表、缓解和局限，未复现。

## 方法与分类

p6表I：HumanEval820、CoderEval Java1,150、Python1,150，共3,120样本，来自DeepSeek-Coder-1.3B/7B、CodeLlama-7B、GPT-4和DeepSeek-R1。人工主题分析得到Requirement Conflicting、Code Inconsistency、Knowledge三类，细分12类。最初500例试标注，两专家建立codebook，之后十名标注者继续。

p13表II列联表：有幻觉且出错1,063；有幻觉而无错71；无幻觉但出错899；无幻觉且无错1,087。总3,120样本中1,134（36.35%）有幻觉。该表直接说明幻觉不等同于全部功能错误，更不能等同于全部安全漏洞。

p13表III：有幻觉样本pass@1=6.26%，无幻觉=54.73%；这是条件统计关联，不能作为漏洞检测precision/recall。

p15表IV：针对DeepSeek-Coder-1.3B的提示缓解，HumanEval原pass@1 61.59，Self-Refine54.27，CoT51.83；CoderEval Python RAG14.78→26.52。任务、模型和基线不同，不能概括所有RAG均提高安全性。上述变化衡量功能/幻觉，不是安全攻击检验。

## 局限与连接

p16–17承认语言和任务范围、人工判断主观性、标注一致性仍可能受限。独立判断：把行为偏离归为“知识幻觉”或“推理错误”需标注规范，不可据单例推断内部成因。课程中适合用于界定生成缺陷边界，安全章节需另加CWE/利用条件证据。

## Word摘要卡

- 研究问题：代码幻觉有哪些类别、可能成因和影响，如何缓解？
- 意义：帮助区分功能错误、知识幻觉和真正安全漏洞。
- 方法：多模型代码生成与人工主题分析，再检验提示和检索增强策略。
- 实验与页码：p6表I共3,120样本；p13表II有幻觉1,134，其中71仍通过功能判定；p15表IV单模型RAG使CoderEval Python pass@1从14.78升至26.52。
- 局限：幻觉标签依赖人工定义，功能与幻觉指标均不能直接替代安全指标。
- 作者写作任务：自行举例说明“通过单元测试仍有幻觉”和“无幻觉仍可能功能出错”。
