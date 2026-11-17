# [02] Rethinking the Evaluation of Secure Code Generation：全文证据笔记

- paper_id: doi:10.1145/3744916.3773217；预印本 arXiv:2503.15554v2。
- 作者：Shih-Chieh Dai, Jun Xu, Guanhong Tao。正式出处：2026 IEEE/ACM 48th International Conference on Software Engineering (ICSE ’26)，336–348（13页）。
- 来源：[正式会议页面](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/175/Rethinking-the-Evaluation-of-Secure-Code-Generation)；[作者正式PDF](https://tao.aisec.world/assets/pdf/ICSE26.pdf)；[可下载预印本v2](https://arxiv.org/pdf/2503.15554v2)；[工件](https://github.com/Utah-SaLT-Lab/RethinkSecCodeEval)。
- 核验日期：2026-11-17；完成方法、结果、局限的全文阅读及关键表格复算。未运行模型实验。以下页码均为PDF顺序页码；正式作者PDF与arXiv v2均为13页，关键表格一致。全文文本保存 sources/rethinking_arxiv.txt。

## 研究对象与流程（论文证据）

- 关注函数级生成技术，不是直接评价当前商业Copilot产品。比较 SVEN、SafeCoder（训练）、CodeGuard+（解码与提示约束）、PromSec（扫描器反馈迭代提示）。见p3–4、表1。
- 同一段生成代码同时接受单元测试与漏洞扫描，避免分别在两个基准测“功能”和“安全”后拼接结论。扫描器为CodeQL、Bearer、Bandit；Qwen2.5-72B和Llama3.3-70B另用于检测器质量诊断。见p4–6。
- BigCodeBench：1,140项Python任务，平均5.6个单元测试；SecCodePLT+：1,201项Python任务，平均7.5个测试。SecCodePLT+通过Qwen2.5-Coder-32B产生输入、执行参考程序产生期望输出构造。见p4表2及§3.2。
- 开源生成模型：CodeLlama-7B、Qwen2.5-Coder-7B、DeepSeek-Coder-V2-Lite、Mistral-7B、StarCoder-1B；商业模型GPT-3.5-Turbo、GPT-4o仅试PromSec。StarCoder不试PromSec。CodeGuard+部分模型缩进先自动修正；其安全提示约束还利用基础模型输出的CWE检测标签，比较条件存在优势。见p5、p8。

## 指标与分母

- Secure@1：按指定扫描器无报警的生成样本占比，不能解释为经证明无漏洞。
- Secure-Pass@1：无任一扫描器报警且所有功能测试通过的样本比例。
- SAFE@k = (1/k) Σ_i secure_i × (exp(case_pass_i)−1)/(e−1)。case_pass是该样本通过测试的比例；secure为三扫描器都不报警的二值判断。SAFE允许功能部分正确，不等于严格功能正确率，且仍依赖测试覆盖及安全判定器。公式见p4式(1)，聚合规则p8。
- 最终联合评价没有使用LLM检测器，因为人工检查显示大量误报；不能描述成“五检测器多数投票”。见p8。

## 关键可核数据

| 证据位置 | 条件和原值 | 能支持的判断 |
|---|---|---|
| p6图5及正文 | Qwen2.5-Coder+SafeCoder / BigCodeBench：CodeQL 0.9877，Bearer 0.6535，Bandit 0.7482 | 同一输出的无报警率依赖检测器；三者不是独立真实安全率 |
| p6表3 | Mistral+SVEN/SecCodePLT+随机44例人工检查：CodeQL TP/TN/FP/FN=2/21/0/19；Bearer=9/15/6/12；Bandit=3/19/2/18；Qwen=20/3/18/1；Llama=21/0/21/0 | 静态检测器漏报与LLM过度报警同时存在；样本量和范围有限 |
| p8表5 | GPT-3.5/BigCodeBench Base→PromSec：Bearer无报警率0.6447→0.7325；全部功能测试通过率0.5078→0.3166；Secure-Pass@1 0.3219→0.2447；SAFE@1 0.4445→0.3810 | 某一安全分数提高可伴随功能和联合指标下降 |
| p9表7 | DeepSeek-Coder/BigCodeBench，仅“不安全且功能正确→扫描安全且功能不正确”的PromSec子集共63例，92.06%分类为删除代码 | 支持特定失效机制，不能写成全部生成代码92.06%被删除 |
| p10图9 | Qwen2.5-Coder用CodeGuard+后引入os.system调用，形成CWE-78例子 | 安全生成干预也可能引入新漏洞，是案例证据 |

### 复算与论文内部不一致（研究者核查，非作者结论）

1. 表3人工样本中真实有漏洞21例、无漏洞21例，合计42？注意表3各行合计42（2+21+0+19=42），而正文称抽取44例。这是另一处需核对工件的样本数不一致，不应强行补出2例。
2. 按表3标准定义 FPR=FP/(FP+TN)：Qwen=18/21=85.71%，Llama=21/21=100%；CodeQL FNR=19/21=90.48%。作者p6的“nearly 50% false positive rate”可能更接近FP/正文44的比例，但未核实其实际分母，不应直接当标准FPR引用。所有数值仅适用于该小样本，不能外推全基准。
3. p8正文称GPT-3.5的SAFE由0.4445降至0.381下降28%；按表5原值复算相对降幅为14.29%，绝对降幅0.0635。Secure-Pass由0.3219降至0.2447的相对降幅为23.98%。报告优先使用原值，并说明文字百分比不一致。

## 局限：作者承认与独立判断

作者在p10–11 §5承认：静态分析器仍会漏报；任务主要是Python；SecCodePLT+测试由LLM生成且未人工全面验证边界覆盖；数据污染不能排除；并未重复所有实验。一次完整运行约430 A100 GPU小时，Qwen重复三次共约1,290小时（p11）。人工安全检查至少两作者审阅，分歧由第三作者解决（p10）。

独立判断：多工具并集减少部分漏报，但可能累计误报；“零报警”的secure_i仍只是操作定义。SAFE的指数映射是设计选择，不能自动表明部分通过的代码具有部署价值。小样本混淆矩阵和全样本扫描分数应分开呈现。没有动态利用验证就不能称每个报警都已证实可利用。

## 与课程研究问题的连接（分析提示，需作者自行形成论证）

- 比较表应同时放功能测试、扫描器规则覆盖、人工核验、联合指标、成本，不能只按安全分数排序。
- FPM方向：分别问误报过滤提升precision多少、漏报是否增加；至少保留TP/FP/TN/FN原始计数和适用范围。
- RAG方向：检索到安全知识后，还须核验版本、代码语境和可执行证据；该论文没有直接证明RAG或FPM一定有效。
- 写作任务：自行解释表5为何推翻“单项安全分数改善就表示代码更好”的推理；自行讨论严格Secure-Pass与宽松SAFE分别适合什么评价目的。

## 下一步复现核对项

- 查工件中表3的42/44样本差异及抽样清单。
- 固定扫描器版本、查询包、忽略规则，复现表5原始计数。
- 单列scanner-union报警的人工复核precision，以及测试输入边界覆盖。

## Word摘要卡

- 研究问题：安全生成技术在同一代码上联合考察功能和安全后是否仍有效？
- 意义：揭示单扫描器评价及功能与安全分离评价会造成误导。
- 方法：四种技术、两个Python基准，联合单元测试与三静态扫描器，并人工诊断检测器。
- 实验与页码：p4表2为1,140与1,201任务；p8表5 GPT-3.5/PromSec的Secure-Pass从0.3219降至0.2447；p6表3混淆计数合计42与正文44不一致。
- 局限：扫描并集仍非真实安全保证，生成测试覆盖和小样本人工核验有限。
- 作者写作任务：自行复算FPR/FNR和表5降幅，解释为何零报警不能作为安全金标准。
