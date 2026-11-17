# [05] Teaching an Old LLM Secure Coding: Localized Preference Optimization on Distilled Preferences

- paper_id: doi:10.18653/v1/2025.acl-long.1263
- 出处：ACL 2025 Long, pp.26039–26057
- 来源：https://aclanthology.org/2025.acl-long.1263/
- 阅读日期：2026-11-17；状态：全文获取并定向阅读方法、主要实验与局限，未独立复现，未逐项复核全部附录。
- 本地来源：sources/paper_05.pdf；sources/paper_05.txt；PDF页码包含封面（如有）。
- 用途：研究笔记与作者独立写作任务；不是可直接提交的综述正文。

## 方法与证据

- DiSCo以CWE/CodeQL/Bandit知识和75个常见Python库构造蒸馏提示，GPT-4o生成同任务的不安全/安全代码对及解释；最终9987条，覆盖431 CWE。§4、§6.1，PDF pp.4–6。
- 一轮静态工具反馈后，所谓安全响应仍含问题的比例37.4%→12.7%；三轮到9.4%，但产生过度设计并损害下游效用。§4.2、表5，PDF pp.4–5、9。
- LPO：先SFT安全解释+代码，再对安全/不安全代码差分token施加偏好损失，其他token加SFT正则，避免通过非解析代码投机。§5，PDF p.5。
- 安全测四组数据：SecurityEval、Asleep、LLMSecEval、DiSCo-Test；CodeQL与Bandit检查所有告警，去重共同告警。InS=有效生成中至少一问题的比例，I@100=每100生成问题数。功能在HumanEvalX/MBXP另测。§6，PDF p.6。
- Phi2-2.7B/CodeLlama7B/Mistral7B/StarCoder2-7B，LoRA r16、alpha32，安全每提示采样5次T0.4。§6.2–6.4。
- StarCoder2在SecurityEval InS56.3%→11.4%、I@10086→20；HumanEvalX pass@1 33.2%→38.9%。表3，PDF p.9（印刷26047）。
- 去掉正则：InS8.0%（更低）但功能pass@1仅27.4%；去掉解释则pass@1 18.8%。表3，PDF p.9。这是“安全分数更好仍可能更差”的直接证据。
- 未见CWE训练设置：SecurityEval InS16.6%、LLMSecEval18.5%，仍优于原模型56.3/65.8%；完整数据训练11.4/12.6%。表4，PDF p.9。

## 可靠性与写作边界

- 【作者自述】闭源模型蒸馏可复现性有限、数据有噪声；基准较小较简单、只评Python；复杂仓库与跨语言需进一步验证。Limitations，PDF p.10。
- 【本次分析】差分token不必然全部都是安全相关token；函数风格或功能差异也可能进入mask。
- 【本次分析】训练和评价都依赖CodeQL/Bandit，应审计工具盲区及产生无效代码的分母；不同数据集功能分数不能证明某个安全修复保功能。
- 独立分析任务：用表3解释reward hacking；以表5解释更多静态修复轮次为何不必然更好；不要用跨模型安全分数推导整体编程能力优于GPT4o。

## Word摘要卡

- 研究问题：如何蒸馏安全偏好并仅强化影响漏洞的局部token？
- 意义：正则消融直接揭示安全评分与功能效用的权衡。
- 方法：DiSCo安全/不安全代码对、差分mask偏好损失与其余token正则。
- 实验与页码：StarCoder2 InS56.3→11.4%，去正则InS8.0%但HumanEvalX pass@1 27.4%（完整38.9%）；InS分母有效生成，每提示5次；表3/PDF p.9。
- 局限：只验证Python，工具与合成数据有噪声，功能安全分集评价。
- 作者写作任务：说明“8.0%更安全”为何不能直接判为更好方法。
