# 软件供应链中大模型代码生成（Copilot）的安全缺陷自动检测

> 审阅稿：保留AI辅助初稿来源，需本人核对与主体二次重构。

## 摘要

大模型生成代码的安全风险贯穿代码补全、依赖推荐、上下文检索与开发者采纳等环节，单纯检查代码可运行或扫描器无报警，难以充分说明输出可靠。本报告围绕二十篇候选研究，从真实项目实证、安全评价、生成期防护、依赖与记忆风险以及后门规避展开分析，并区分直接检测方法与改变生成行为的干预技术。跨论文比较表明，功能与安全分集评测、类别偏斜、判定器误差及成功定义差异，会限制安全分数的解释；检索增强也需区分类型判断、评论质量与版本适用性。报告据此讨论带漏报约束的误报过滤、版本与可达性约束下的证据验证，以及跨威胁的功能安全联合评价。这些方向属于待验证研究建议，尚无本项目实验结果。可信检测的核心在于保留可追溯证据、明确适用边界，并在同一输出上检验风险控制与功能效用。

**关键词：** 大模型代码生成；软件供应链；漏洞检测；误报过滤；检索增强生成；安全评价

## 第一部分：选题依据与文献分类综述

大模型代码生成将训练数据、检索示例、第三方依赖与开发者采纳连接起来，使安全缺陷的来源超出生成代码本身。真实仓库研究揭示了生成片段中的安全弱点[1]，依赖包研究展示了不存在包名形成的潜在供应链攻击面[2]，开发者实验则说明受污染建议可能进入实际实现[3]。这些证据共同构成研究自动检测与验证的动机，但报警、风险建议和已发生的入侵具有不同含义，不能合并为单一漏洞率。

本报告围绕二十篇候选研究，按“缺陷实证与评价—检测及生成期防护—依赖与记忆风险—投毒及检测规避”组织材料。实证与评测研究用于界定风险和测量误差；静态扫描、模型审查及检索增强研究用于比较发现问题与约束输出的机制；后门和规避研究用于检验检测前提。其中，[4]研究代码摘要与命名任务，且本次取得的是较早作者稿，仅作为边界对照，不承担可执行漏洞生成的核心证据。

分析主线由三篇论文展开：Rethinking检验安全分数与功能正确性的关系[5]，CoV-Eval区分生成、检测、分类和修复能力[6]，SecureReviewer讨论安全审查的类型预测与评论质量[7]。报告据此聚焦三个问题：风险如何进入开发流程，自动方法究竟验证了什么，以及安全改进能否在保留功能时成立。题名保留课程中的Copilot表述，逐篇讨论则严格区分商业产品、开源代码模型与受控模拟助手，避免将不同研究对象的结果直接外推。

## 第二部分：单篇论文深入剖析

本部分围绕研究问题、研究意义、核心方法和实验结论逐篇分析，并结合各论文的实验条件讨论方法的适用范围。

### 2.1 [1] Security Weaknesses of Copilot-Generated Code in GitHub Projects: An Empirical Study

该研究考察公开GitHub项目中标注为AI生成的代码包含哪些安全弱点，以及Copilot Chat能否帮助修复，价值在于补充受控提示基准之外的开发场景证据。作者先通过归属注释检索代码，再联合CodeQL与Bandit或ESLint扫描，人工检查报警及其是否位于AI生成片段，避免把邻近人工代码的问题归给生成工具。作者稿Table2统计733份代码，其中Copilot占672份，其余来自另两种助手；Table4显示其中200份包含弱点，弱点实例共628个，因此文件比例和实例数量必须分别解释。修复实验以295个待修CWE问题为起点，增强提示后剩132个，Table7据此报告55.5%的修复率；该结果表示所测问题减少，并未证明修复保持原有功能。研究还显示不同漏洞类别的修复效果差异明显，因而总体均值不足以说明高风险类别得到同等保护。其局限包括自报使用AI带来的选择偏差、人工归属的不确定性、语言范围和分析器覆盖限制。该文支持“扫描与人工核查需要配合”的判断，但缺少同任务的人类对照，也不能由报警过滤结果推得未报警代码的漏报率，更不能据混合样本推断当前Copilot产品的整体漏洞率。


### 2.2 [5] Rethinking the Evaluation of Secure Code Generation

该研究追问安全代码生成技术获得更好安全评分时，是否仍能完成原始功能，贡献在于把评价对象重新统一到同一份生成代码。作者比较训练、解码约束及扫描反馈等四类技术，在两个Python基准上同时运行单元测试与CodeQL、Bearer、Bandit，并以人工检查诊断检测器误差。严格联合指标要求功能测试全部通过且三种扫描器均不报警，SAFE则允许部分功能测试通过，因此两者表达的效用不同。Table5中，GPT-3.5在BigCodeBench采用PromSec后，Bearer无报警率由0.6447升至0.7325，功能全通过率却由0.5078降至0.3166，联合通过率由0.3219降至0.2447，构成单项评分改善不能替代整体质量的直接反例。该研究也提醒静态漏报与模型判定器过度报警可能并存，多工具组合仍不是安全证明。证据核查发现，Table3各行混淆计数合计42，而正文称抽样44；Table5对应的SAFE降幅文字也与表值不符，故应保留原计数和原值，不把冲突百分比直接用于推论。研究主要覆盖函数级Python任务，自动生成测试的边界覆盖与数据污染风险仍有限制，其结果支持联合验证的必要性，尚不能保证复杂仓库或全部输入条件下的安全。


### 2.3 [6] Can You Really Trust Code Copilot? Evaluating Large Language Models from a Code Security Perspective

该研究将代码补全、漏洞修复、漏洞检测和CWE分类分开评价，解决仅凭代码可运行或单项检测分数判断模型安全能力的问题。作者以54个种子场景扩展270个场景，构建CoV-Eval，并微调Llama3-8B形成VC-Judge，使其结合已知场景的漏洞类别和描述判断输出。Table1显示GPT-4o检测F1为94.62%，而CWE分类F1为36.05%，说明发现可疑代码、判断具体类型与生成安全实现不能合为一种能力。评测工具本身仍需校准：Table5中VC-Judge与人工判断的一致性随种子、扩展和修复集合变化，未达到完全一致。尤其Table8的检测集由477条漏洞与54条无漏洞代码组成，存在明显类别偏斜；按该计数复算，全部判为有漏洞也可获得94.64%的阳性F1，因而高分不能单独证明模型能够辨别安全代码。论文虽称采用加权F1，具体结果与阳性F1口径的对应仍需脚本核实，不宜径直认定实现错误。此外，功能与安全分别在不同数据集评价，尚不能证明同一修复保持原任务功能；依赖已知CWE提示的判定也不能直接代表开放世界发现能力。该文的意义在于建立能力分解与判定器校准的比较框架，而非给出无误报自动检测的终局方案。


### 2.4 [8] SecCoder: Towards Generalizable and Robust Secure Code Generation

SecCoder研究安全生成如何适应训练中未覆盖的漏洞类别，以及能否缓解模型受到不安全前缀干预后的行为退化，工程意义在于不更新目标模型参数即可增加安全示例。方法先构建已修复代码演示库，再利用INSTRUCTOR表示和余弦相似度检索一个示例，与待补全上下文拼接，通过上下文学习引导冻结模型生成。实验覆盖九类CWE，涉及C/C++与Python；其安全率以每个提示采样后去重、且编译或解析有效的输出为分母，由CodeQL判断是否存在报警。Table1中，受SVENvul干预的CodeGen-350M安全率由35.02%升至44.89%，说明检索示例在特定攻击条件下能够恢复部分扫描表现。该结果不能直接解释为自然开发环境的漏洞下降，也不能与保留所有失败输出的评测直接排序。更关键的是，所谓未见类别主要针对基线训练，而演示库包含评价类别，因此泛化并不意味着完全缺少相应安全知识。方法依赖示例库本身可靠，知识污染和补丁适用性仍需另行检查；功能在HumanEval上独立评价，也未证实原任务中的同一输出同时满足功能与安全。由此，该文适合作为检索式生成防护的代表，与生成后审查互补，但不应归为对任意代码进行漏洞确认的检测器。


### 2.5 [9] Teaching an Old LLM Secure Coding: Localized Preference Optimization on Distilled Preferences

该研究关注如何让已有代码模型学习安全偏好，同时减少安全优化对一般编程能力的损害。作者构建DiSCo数据，利用漏洞知识和库使用场景蒸馏同任务的安全与不安全代码及解释，再通过局部偏好优化强化差异位置，并对其余位置施加监督正则。其意义是把训练信号尽量聚焦于代码修改，而不是笼统奖励整段“看起来安全”的输出。实验用CodeQL与Bandit评价有效生成中的问题比例，并在其他功能基准上检查效用。Table3中，StarCoder2在SecurityEval上的InS由56.3%降至11.4%，HumanEvalX的pass@1由33.2%升至38.9%；但移除正则后，InS进一步降至8.0%，功能分数却只有27.4%，表明更低的问题率可能伴随明显效用损失。数据构造也呈现类似权衡：更多静态反馈轮次继续压低问题比例，却可能引发过度设计。其局限在于训练与评价依赖相近扫描工具，闭源模型蒸馏的数据噪声难完全排除，且主要覆盖Python与较小任务。安全和功能分集评价也不能替代同一代码的联合验收。因此该文既提供训练防护方法，也提供反思评价目标的消融证据，尤其适合说明降低扫描问题率必须同时考虑有效输出与功能保留。


### 2.6 [7] SecureReviewer: Enhancing Large Language Models for Secure Code Review through Secure-Aware Fine-Tuning

SecureReviewer面向代码差分的安全审查，目标是同时识别问题类别并给出包含描述、影响和建议的结构化评论，其价值在于将安全判断与开发者可执行的审查意见联系起来。方法从真实拉取请求构建数据，通过安全感知损失加权代码标识符和安全类型，结合LoRA微调；随后按预测类型从评论模板中检索内容，改写其他字段。Table1的测试集为300条，而评论生成只评价其中262条安全样本，两类分母不能混用。Table2中CL版本F1为71.98，最佳基线为61.46，但这一分类改善不能归因于后续检索，因为RARG明确保持安全类型不变。Table3进一步显示，CL版本加入检索后SecureBLEU从29.69降至29.31，说明模板知识对已微调模型并无一致增益。该指标衡量评论结构与安全关键词等特征，不能替代漏洞可利用性、补丁有效性或功能保持检验。差分输入缺少跨过程调用语境，且无评论样本被用作Non-Issue存在标签风险，都会限制结论迁移。因而，该文更适合支持领域训练如何改进审查类型和建议质量，并提醒分别评价检索、分类与评论生成，而不能据此声称RAG已经提高漏洞检测F1或证明代码安全。


### 2.7 [10] Repairing LLM Executions for Secure Automatic Programming

该研究探索能否在生成过程中识别并修复导致不安全代码的模型内部表征，使防护从提示和输出扫描扩展至推理激活。THEA以稀疏自编码器分解残差流，比较安全与不安全样本的特征分布，筛选候选特征并干预激活，再通过输出检测验证效果；它修复的是模型执行状态，而非直接修改已经生成的源代码。实验基于Llama3.1-8B，并以ICD作为检测工具。Table1中，1916个CyberSecEval提示产生的总告警从576降至489，即按原告警数复算减少15.10%；功能测试则有小幅下降，InstructHumanEval由71.9%变为70.1%，因此不能将效果概括为完全没有性能代价。其价值在于提供模型内部控制与预警的研究路线，但需要访问激活及适配的自编码器，无法直接充当黑盒商业助手的外部扫描器。证据还有两项边界：特征选择与验证依赖同一检测器，可能继承共同盲区；部分漏洞减少比例在正文与Table2间不一致，另有正文193例与Table3计数210例的差异。对此应优先保留一致总数，不拼接冲突分项。该文说明内部干预可以减少所测报警，尚未证明所有语义漏洞消失，也不能免除独立功能回归和安全确认。


### 2.8 [11] GoodVibe: Security-by-Vibe for LLM-Based Code Generation

GoodVibe关注模型在用户未明确提出安全要求时，能否以有限训练开销改善默认生成行为。其意义在于把安全防护从输出后的报警处理前移到模型内部，同时为参数规模与训练计算提供比较依据。方法首先通过监督安全判断任务的梯度归因筛选安全相关神经元，再按激活模式聚类并限制更新范围，从而避免对全部参数进行微调。研究使用同提示的安全与不安全代码对，在六个开源模型上评测；表1报告，六模型的平均安全判定比例在C++任务中由35.1%升至87.5%，在Java任务中由59.3%升至76.0%，各比例的分母是对应模型条件下的测试输出。表2中的平均可训练参数为1.9M，说明局部更新具有减少训练参数的潜力。不过，这些安全标签来自独立微调的语言模型判定器，其分数反映测量工具的判断，不能直接理解为经证实的漏洞消除率。论文还在其他任务上单独测量功能表现，尚不足以证明每份安全输出保持了原任务功能。因此，该工作为生成期防护提供了内部控制路线，但其证据仍受判定误差、任务范围与仓库上下文覆盖限制，不能替代生成后的独立程序验证。


### 2.9 [12] Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection

CodeGuarder研究检索增强代码生成中的安全知识缺失问题：功能相似的示例可能包含漏洞，仅增加相关代码未必能够形成可靠防护。其价值在于将检索内容从可复用实现扩展到漏洞根因与修复依据。系统离线从真实漏洞版本、补丁及CVE/CWE中提取“功能—根因—修复模式”，在线把功能请求分解为子任务，通过向量检索、风险加权排序和过滤，将适用的安全知识注入生成提示。研究覆盖四个模型和四种语言，并设置两类检索投毒条件。作者稿表4报告，标准检索生成条件下的平均安全判定率由60.84%升至73.08%，增加12.24个百分点；统计基于各模型、语言条件的生成输出，其平均值不能解释为自然开发分布中的总体漏洞率。该结果支持根因与修复知识在所测场景中的应用价值，但安全判定依赖CyberSecEval的ICD检测器，CodeBLEU也只是代码相似度代理，二者不能共同证明语义正确且无漏洞。补丁知识还需要保留来源与版本，避免模型提取错误或高频漏洞权重掩盖低频问题。本报告依据可访问作者稿讨论方法与实验，其页码不等同于正式CCS出版页码；该方法也尚不能作为任意知识库投毒均已被识别的证据。


### 2.10 [13] Securing Retrieval-Augmented Code Generation via Contextual Knowledge Injection: A Case for Embedded IoT Applications

IoTRAGuarder将安全知识的适用性具体化为版本、公共API与漏洞触发路径，研究生成应用如何经固定RTOS或SDK继承内部历史漏洞。其工程意义是解释为什么表面安全的接口使用，仍可能调用底层有缺陷实现。系统从CVE内部函数逆向恢复到公共API的调用关系，以静态分析和受证据约束的语言模型补充宏或间接调用信息，再把版本区间、触发条件、替代接口及升级建议写入安全知识库，在线进行功能与安全双层检索。ZEVULBENCH由Zephyr的九个已知CVE衍生四十四项任务，四模型形成一百七十六个模型—任务案例。表6报告，原CodeGuarder成功9/176，替换上下文安全库后为113/176，完整系统达到138/176，即78.41%。但成功既包括应用层安全实现，也包括无法在应用层缓解时给出正确API或版本警告并建议升级，因而该比例不能改写为可运行无漏洞程序比例。该研究说明调用可达性和版本匹配值得进入供应链安全核验，同时仍受已知漏洞范围、路径分析覆盖和人工判据约束；它既未证明未知漏洞检测能力，也未完成跨RTOS验证。比较其他RAG方法时，应先对齐成功定义，再讨论知识注入收益。


### 2.11 [14] Beyond Functional Correctness: Exploring Hallucinations in LLM-Generated Code

该研究讨论代码幻觉的类别、影响及缓解方法，为区分生成缺陷与安全漏洞提供了概念基础。论文从多个模型在HumanEval和CoderEval上的输出中取样，通过人工主题分析建立需求冲突、代码不一致和知识幻觉三大类、十二个细分类别，并考察这些标签与功能结果的联系。表I共列出三千一百二十份代码样本；表II中，一千一百三十四份被标记有幻觉，其中七十一份并未在功能判定中出错，同时还有八百九十九份无幻觉代码发生功能错误。这一列联关系说明幻觉标签与功能失败并不等价，更不能将其直接当作安全漏洞标签。研究还比较提示与检索等缓解方法，表IV中针对DeepSeek-Coder-1.3B的RAG使CoderEval Python的功能pass@1由14.78%升至26.52%，但这一结果属于特定模型与任务的功能评价，不能据此认定安全性同步提高。该工作的意义在于使检测对象的定义先于指标比较：需求偏离、虚构知识和可利用漏洞需要不同的证据。其局限包括人工分类的主观性、语言与任务覆盖，以及对内部成因解释的间接性。因此，安全报告可借用其分类厘清风险边界，但仍须通过CWE、触发条件或运行证据确认具体安全问题。


### 2.12 [2] We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs

该论文把生成代码风险延伸到依赖解析环节，研究模型推荐不存在软件包的频率、重现性与缓解代价。它的重要性在于说明，代码正文即使看似合理，也可能把开发者引向缺乏真实来源的依赖名称，形成潜在的软件供应链攻击面。研究针对十六个模型生成Python和JavaScript代码，累计取得五十七万六千份样本，再结合安装命令与依赖询问等启发式抽取分发包名，并核验包仓库及时间条件。正文报告，约二百二十三万次包名出现中，440,445次被判为幻觉，占19.7%；分母是包名出现次数，不能解释为19.7%的程序存在安全漏洞。对已发现幻觉的提示重复测试还显示部分名称稳定重现，但这种条件抽样不代表所有用户请求的风险发生率。缓解也存在功能代价：表5中DeepSeek微调后的pass@1由51.4%降至25.3%，说明仅压低幻觉指标可能牺牲任务完成能力。作者没有通过发布恶意幻觉包制造真实受害事件，因此现有结果支持潜在攻击面的存在，并未证明实际安装受害率。对自动检测而言，模块名与分发包名映射、注册时间和包来源都需核查；名称存在也不能保证其内容可信。


### 2.13 [15] HFuzzer: Testing Large Language Models for Package Hallucinations via Phrase-based Fuzzing

HFuzzer研究如何主动生成测试输入，以更系统地发现模型的依赖包幻觉。相较固定提示集，它的意义在于提供可重放的触发案例，并通过反馈扩大已发现风险的覆盖范围。方法从真实软件包描述中抽取短语种子，组合开发任务，查询目标模型生成代码与依赖信息，再根据包仓库核验结果和新幻觉发现调整种子权重、扩充种子池。实验以Python为主要生态，九种模型分别承担测试生成者与目标角色，形成八十一个组合。表II报告，相对作者适配的GPTFuzzer-A，独特幻觉包数量平均达到2.60倍；图5报告的2.36倍则对应任务多样性指标，两者既不是同一分母，也不是自然使用时的幻觉发生率。论文PHR按含幻觉包的响应数除以总响应数计算，与包名出现次数比例亦不可混用。其局限是抽取规则、种子来源和采样预算影响覆盖，模块名、分发包名与跨语言名称还可能造成误判。部分模型的低PHR可能来自过度拒答，因而应同时记录任务完成与有效输出情况。该工作补充了依赖风险的主动测试能力，但不能作为对任意现成程序的通用漏洞检测器，更不能把主动诱发结果直接外推为真实供应链入侵率。


### 2.14 [16] Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis of Public GitHub Repositories

该研究扩大了公开仓库中AI归属代码的观察规模，试图分析不同语言和助手对应的弱点分布。其价值是把研究对象从受控提示输出推进到实际开发仓库，同时暴露生成归因和统计口径的困难。方法以显式AI注释检索文件，经去重、语言和大小筛选后使用CodeQL扫描，再按工具与语言汇总。表2从82,413个原始文件筛至10,387个，其中表3记录ChatGPT文件9,506个、Copilot文件779个，工具样本明显失衡。然而，进入最终分析的文件分母在摘要、正文与表5中分别出现7,703、7,117和7,696，尚不能选择其中之一作为已确认总体。表6列出的861个带CWE文件与4,241个实例，也混有未使用变量等质量问题，不能全部称为经证实可利用的漏洞。因此，本报告保留规模、方法及分母冲突，不采用其整体安全率或据此排列助手安全性。显式注释还不一定精确界定AI生成片段，静态工具无法穷尽运行时和逻辑问题；类别映射的平均CVSS也不等于每个样本的严重度。该工作提示真实场景研究需要把采样、代码归属、告警分类和人工确认分别留证，否则更大的样本仍可能得到难以解释的安全结论。


### 2.15 [17] Insecure Coding Preferences in Long-Term Memory: Security Risks for LLM-based Code Generation

该研究关注长期记忆中保存的不安全编码偏好，是否会持续改变后续代码生成的安全性，将分析对象从训练数据和即时提示扩展至推理期的持久输入依赖。作者通过开启、关闭记忆的配对实验，结合功能测试、安全测试和人工警告标注，考察生成质量及风险提示。可访问扩展作者稿采用100个Python任务和94个非Python任务，每任务生成三次；其表1报告，Python上跨k=1、2、3的平均Vul@k，ChatGPT由59.5%升至73.3%，Gemini由62.7%升至74.0%。这些数值反映多候选指标的平均变化，不能解释为单次生成漏洞率。论文的价值在于揭示：不修改模型权重，历史偏好仍可能形成跨任务的风险来源，因而记忆条目也需要安全审查。不过，正式会议摘要仅讨论两个模型，扩展稿增加至四模型，实验范围须按版本区分。扩展稿中记忆过滤的全部检出结果来自预选高风险子集，尚不足以证明开放分布中的低误报和高召回；记忆污染也不应与权重后门混为一谈。


### 2.16 [18] TrojanPuzzle: Covertly Poisoning Code-Suggestion Models

TrojanPuzzle研究训练集中的危险代码扫描能否阻止代码补全模型被投毒，其核心意义是区分“训练样本没有显式危险片段”与“模型不会生成危险代码”这两个命题。论文比较SIMPLE、COVERT和TrojanPuzzle，考察模型学习上下文与输出替换关系后，危险行为能否在补全阶段出现，并在CodeGen 350M和2.7B上验证。作者稿§6.2和图9中，350M模型使用八万份训练文件，其中160份为投毒文件，占0.2%；跨四类漏洞试验及三轮微调，TrojanPuzzle的平均attack@10为20.42%，COVERT和SIMPLE分别为41.25%和41.88%。attack@10表示十个候选中至少一次攻击成功，不能改写为Copilot单次补全的漏洞比例。这组结果显示，隐蔽机制与攻击成功率存在需要分别衡量的取舍，不能只选择最高成功率评判攻击能力。对自动检测而言，论文揭示的是特定训练清洗防线的覆盖边界；若生成后的显式漏洞仍可被扫描器识别，后置验证依然可能发挥作用。因此，训练规避成功不足以证明整个供应链防护失效，结论还受模型、漏洞类型和可访问作者稿版本约束。


### 2.17 [19] An LLM-Assisted Easy-to-Trigger Backdoor Attack on Code Completion Models: Injecting Disguised Vulnerabilities against Strong Detection

该论文将检测规避问题从训练集清洗进一步推进到生成后的代码审查：即使危险行为已经进入输出，静态分析器与大模型是否仍能识别？其CODEBREAKER框架利用大模型辅助变换危险载荷，并比较触发形式、静态规则及模型审查结果，研究行为保留与表面模式变化之间的关系。表3在jinja2、文本触发、第一轮训练条件下报告，CB-GPT使40个提示中的23个出现危险补全，而400份补全中185份危险；前者是提示层面的至少一次成功，后者是补全层面的比例，二者不能混用。同一表中，SIMPLE产生的154份危险补全经所测后置检测后降为零，说明输出检测能阻断某些攻击，却可能被更隐蔽的变体削弱。其贡献在于为检测器提供对抗性反例，促使安全评价检查语义行为而非只确认规则未命中。不过，论文仅检验特定工具、版本与漏洞集合，部分工具对部分漏洞不适用；表6也存在未完全规避的情形。因此，它不能支持“绕过所有工具”的概括，也未提出完整的防御方案。训练阶段与输出阶段的风险应分开记录，再通过独立证据检查剩余漏洞。


### 2.18 [4] Stealthy Backdoor Attack for Code Models

该研究考察自适应触发器能否逃避代码模型后门检测，主要回答固定触发模式下形成的检测经验能否迁移到更隐蔽的输入变化。AFRAIDOOR通过保持程序语义的自适应扰动构造触发条件，在CodeBERT、PLBART和CodeT5上考察代码摘要与方法名预测任务，并比较谱特征等防御。可访问作者稿表7显示，在代码摘要的CodeBERT设置中，攻击成功率为98.53%，经过防御后仍为96.35%；固定触发器则由100%降至8.27%。这些数字表明，所测防御对不同触发机制的效果存在明显差异，但其分母和目标是攻击输出命中，不能解释为漏洞检测召回率或不安全代码生成率。论文对本报告的意义是提供检测泛化的边界证据，提示检测器可能依赖攻击留下的特定统计痕迹。不过，摘要和命名任务不直接检验可执行补全中的安全缺陷，迁移至Copilot式代码生成仍需补充实验。另需指出，本次可读全文为2023年预印本旧稿，含模板页眉与占位内容，尚未取得出版社最终稿。因此该文仅承担辅助威胁分析，其旧稿数值不得冒充2024年正式版本已完成核验的结论。


### 2.19 [20] Generalized Adversarial Code-Suggestions: Exploiting Contexts of LLM-based Code-Completion

该研究关注上下文触发条件与危险补全之间的映射能否泛化，以及训练清洗和后门防御能否发现这种关系。作者形式化触发模式和嵌入映射，比较identity、directional和prompt-indexing策略，在CodeGen模型上检验静态分析、近重复、谱特征及剪枝等防线，使攻击比较从名称罗列转向触发机制与覆盖条件。作者稿表2在2%投毒、CWE-22触发提示条件下，350M、2B、6B模型的平均补全成功率ASRø分别为66%、37%、67%，而ASR@10分别为84%、70%、93%，反映多候选攻击与平均补全统计的差别。表1另显示，350M模型在干净提示下的CWE-22 ASRø为5%，触发后为66%，说明评价还应保留干净输入上的误触发对照。对于自动检测，论文支持把上下文行为变化与训练样本异常联合审查；但不同漏洞的规避结果并不一致，例如表7中部分漏洞的投毒样本未被静态扫描命中，另一类仍有命中。因而不能概括为攻击完全不可见，也不能由某个漏洞的模型规模趋势推导普遍规律。结论仅适用于所测模型、数据和防线。


### 2.20 [3] Poisoned ChatGPT Finds Work for Idle Hands: Exploring Developers' Coding Practices with Insecure Suggestions from Poisoned AI Models

该论文考察受污染助手的危险建议是否会被开发者采纳，从而把模型输出风险连接到实际软件实现。研究由238人问卷及30名专业开发者的受控实验组成；实验将开发者分为补全、生成和无工具三组，每组十人，完成AES、SQL和DNS相关任务。作者稿表2中，生成组十人有九人的SQL实现出现注入问题，均被归因为采纳污染建议；补全组八人存在该问题，其中三人被归因为污染建议。这一划分揭示，代码中存在漏洞与漏洞由助手引入是不同结论，必须追踪建议采纳过程。尤其无工具组也有九人的SQL实现不安全，因此不能把全部不安全结果或组间差异笼统归因于AI。论文的工程意义在于说明检测应覆盖建议采纳和代码集成环节，而不只报告模型生成时的攻击成功率。然而，实验采用ChatGPT-like与IntelliCode-like受控工具，并不意味着真实ChatGPT已被攻破；样本较小、任务有限，也难以直接代表日常开发。该文为开发工作流中设置检测与复核提供动机证据，但未提出新的检测算法，更未证明人工审查必然无效。


## 第三部分：整体深度综述与前沿展望

### 3.1 从风险来源界定检测边界

这些研究首先要求区分“生成结果有缺陷”和“模型受到恶意控制”。自然生成的漏洞可能来自不安全编码模式或上下文不足；训练投毒则要求攻击者影响学习数据，并在特定条件下诱导危险补全[18][20]。长期记忆中的不安全偏好属于推理输入的持续影响，不能直接归为权重后门[17]。依赖包幻觉还涉及包名解析、注册时间与安装行为；不存在的包名提供潜在攻击机会，却不足以证明恶意代码已经被安装执行[2][15]。因此，检测目标应具体到代码弱点、危险行为、依赖真实性或触发条件，不能用统一“安全率”替代威胁模型。

开发工作流进一步改变了风险的解释。公开仓库中的生成归属通常依赖注释和检索线索，弱点是否位于AI生成片段内仍需核对[1][16]。开发者采纳实验连接了建议与实现，但无工具组也可能产生漏洞，故不能把全部不安全实现归因于助手[3]。从模型输出到软件供应链损害，尚有采纳、依赖解析和部署等环节。报告更适合比较各防线能够确认或遗漏什么，而非从一次攻击成功推断整条供应链均已失守。

### 3.2 方法互补及其工程前提

静态分析适合作为可重复的初始检查，能保留规则、源码位置及部分数据流证据；其局限是覆盖依赖规则和环境，报警也可能缺少实际利用条件。多工具并集能够补充部分覆盖，却可能累积误报；多个工具一致也不意味着误差独立。[5]的小样本诊断和[19]的规避实验分别显示了常规漏检与对抗性盲区。LLM可以补充语境解释，但自然语言解释的完整程度不能代替漏洞真值。[6]面向特定CWE的判定，与开放环境中发现未知类别问题也有不同前提。

生成期防护则作用于不同位置。SecCoder通过安全示例引导冻结模型[8]，LPO利用差分token进行偏好优化[9]，THEA干预内部激活[10]，GoodVibe调整选定神经元[11]。它们可降低特定评价下的危险输出，但并不因此成为可直接部署的生成后检测器。尤其是激活干预需要模型内部访问，不能直接移植到仅提供接口的商业助手。工程选择应同时考虑模型可访问性、训练代价、推理延迟、知识维护和人工复核，而不能只比较可训练参数数量；计算量减少也不等于实测运行时间同比减少。

成本比较还需要明确计量边界。离线知识构建、模型训练与每次请求的在线检索属于不同支出，不能把一次训练开销与单次审查调用直接并列。迭代修复方法还可能通过更多轮调用换取较低报警率，因此应固定调用预算，或同时报告收益随预算的变化。对开发者而言，最终保留下来的可用代码数量和复核时间，比单独的模型调用价格更接近实际价值。现有论文并未在统一环境中给出这些成本，报告只能比较成本构成，不能推断某一方法普遍最便宜。

检索增强的关键差异在于知识如何适配当前代码。SecureReviewer按已预测类型检索评论模板，并保持类型预测不变[7]；CodeGuarder提供功能、根因和修复知识[12]；IoTRAGuarder进一步绑定版本、公共API和内部漏洞路径[13]。三者分别面向审查表达、生成约束和依赖上下文，不能统称为“RAG提升漏洞检测准确率”。检索内容是否真实、版本是否匹配、调用路径是否可达，应与评论是否流畅分别检验。否则，模型可能给出专业但不适用于当前程序的建议。

|路线|主要输出|必要条件或成本|验收时需要补充的证据|
|---|---|---|---|
|静态扫描与组合工具[1][5]|报警和位置|可分析的代码、规则及环境|误报复核、漏报抽检与利用条件|
|多任务评判[6]|检测、分类或修复评分|标签、判定提示及模型调用|类别分布、独立校准与同代码功能测试|
|安全审查[7]|安全类型及评论|代码差分、领域微调、模板维护|上下文适用性与真实问题确认|
|训练或激活干预[9][10][11]|受约束的生成输出|训练资源或模型内部访问|独立检测、功能保持及推理开销|
|知识注入[8][12][13]|示例、根因或版本/API约束|可信知识与更新、检索调用|来源、版本、可达路径及冲突裁决|
|依赖测试[2][15]|不存在包名及触发输入|包名映射、仓库查询与时间快照|真实安装语义、可注册性和任务完成率|

表中比较为本报告综合归纳；各路线作用不同，不能据此形成统一性能排名。

### 3.3 从单项分数转向可审计的联合评价

评价协议是跨论文比较最容易失真的环节。[5]中，GPT-3.5在BigCodeBench上采用PromSec后，Bearer无报警率由0.6447升至0.7325，但功能全通过率由0.5078降至0.3166，Secure-Pass由0.3219降至0.2447。安全单项分数的上升因而不足以证明整体改进。该反例支持在同一输出上联合验证；它不支持所有安全干预必然损害功能的普遍结论。LPO的正则消融[9]和包幻觉缓解中的功能下降[2]也表明，降低被测风险可能伴随任务效用损失。

设N为预先登记的全部生成尝试数，包含拒答、解析失败与最终被过滤项；F为最终保留且通过全部预设功能测试的样本集合，S为选定安全检查通过的样本集合，则联合通过率为|F∩S|/N，功能通过后的条件检查通过率为|F∩S|/|F|。当|F|为零时，条件通过率未定义。二者应同时保留，并分别登记各类失败和过滤数量。S只具有给定检查下的操作含义，不能被解释为已证明不存在漏洞；安全测试或扫描规则遗漏的性质仍不可见。允许部分测试通过的SAFE则是另一种效用设计，与严格联合通过率回答不同问题，其权重选择也应明确说明。

检测指标还受类别分布影响。[6]检测集包含477个漏洞样本和54个无漏洞样本；本报告复算，全部判为有漏洞时，阳性F1已为2×477/(2×477+54)≈94.64%。这不意味着论文所有模型均采取该策略，却说明孤立的高F1不足以证明区分能力。论文文字所称加权F1与部分表值的口径仍需评价脚本确认。Precision、Recall、FPR和FNR应附原始混淆计数，不能把报警中的误报占比或FP/N称为标准FPR；判定安全率的净偏差也可能由误报、漏报相互抵消。

标签来源也应进入可靠性分析。[7]以无审查评论样本构造Non-Issue类别，缺少评论本身却不能证明不存在漏洞；这是对数据构造的有效性疑问，而非已经证实的错误标签比例。类似地，使用同一静态工具产生训练反馈和最终评分，可能共同保留该工具的盲点。更稳妥的复核应优先覆盖工具分歧、被抑制报警及看似安全的负例，并保留双人审查与分歧裁决。跨项目和版本验证也需同步固定模型、规则及依赖快照，避免把环境变化误解释为方法改进。

成功定义同样影响结论。[13]将正确的版本/API安全警告计入成功，78.41%因而不能改写为可运行且无漏洞程序的通过率；[7]的SecureBLEU评价评论，不能代替漏洞利用或补丁回归测试。后门研究中的attack@10与单次补全比例、包名出现级与响应级幻觉率，也应分别报告。对[5][10][16]的内部计数冲突，本报告保留一致的原始表值和争议，不自行补造样本。这样处理虽降低了汇总的简洁性，却能保留结论的可核查范围。

### 3.4 三个值得验证的研究方向

第一个方向是带漏报约束的误报过滤。可在同一批代码和初始报警上比较原始扫描、LLM过滤与RAG过滤，并同时复核保留报警、抑制报警和原始未报警代码。重点是减少多少人工审查，以及错误抑制了多少真实漏洞。若仅标注保留下来的报警，过滤器可能靠删除困难样本获得较高精确率。采用抽样时还需保存抽样概率，避免将复核子集的类别比例直接外推总体。可接受的漏报增加阈值应在实验前声明，并结合估计的不确定性判断，而不能看到结果后选择有利阈值。该方案是本报告建议，现有材料没有验证其收益。

第二个方向是版本与可达性约束下的检索证据验证。可设置正确与过期文档、匹配与错误API版本、可达与不可达路径以及冲突知识对照，分别测量证据引用正确性、最终漏洞判定和错误抑制率。这将问题从“是否检索到安全知识”推进到“知识是否适用于当前代码”。相对既有模板或根因注入方法，其增量价值仍需等成本对照，不能仅凭设计差异宣称创新。

第三个方向是跨威胁、保功能的验证闭环。自然漏洞、训练投毒、包幻觉和记忆污染应分别设置任务，再在同一生成或修复结果上执行功能测试与安全检查。训练与测试按项目、时间或CWE划分，同时保存代码、依赖版本和每步判断。跨威胁结果可以检验方法边界，但不能合并成单一攻击成功率。若收益依赖特定判定器、转移后消失，或主要来自拒答与功能损失，就应收缩有效性主张。可信的自动检测因此更需要可追溯、可反驳的验证过程，而不只是更高的汇总分数。



## 参考文献

[1] FU Y, LIANG P, TAHIR A, et al. Security Weaknesses of Copilot-Generated Code in GitHub Projects: An Empirical Study[J]. ACM Transactions on Software Engineering and Methodology, 2025, 34(8): Article 218, 1–34. https://doi.org/10.1145/3716848

[2] SPRACKLEN J, WIJEWICKRAMA R, SAKIB AHMN, et al. We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs[C]// 34th USENIX Security Symposium, 2025, 3687–3706. https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen

[3] OH S, LEE K, PARK S, et al. Poisoned ChatGPT Finds Work for Idle Hands: Exploring Developers' Coding Practices with Insecure Suggestions from Poisoned AI Models[C]// 2024 IEEE Symposium on Security and Privacy (SP), 2024, 1141-1159. https://doi.org/10.1109/SP54263.2024.00046

[4] YANG Z, XU B, ZHANG JM, et al. Stealthy Backdoor Attack for Code Models[J]. IEEE Transactions on Software Engineering, 2024, 50(4): 721-741. https://doi.org/10.1109/TSE.2024.3361661

[5] DAI S, XU J, TAO G. Rethinking the Evaluation of Secure Code Generation[C]// Proceedings of the 2026 IEEE/ACM 48th International Conference on Software Engineering, 2026, 336-348. https://doi.org/10.1145/3744916.3773217

[6] MOU Y, DENG X, LUO Y, et al. Can You Really Trust Code Copilot? Evaluating Large Language Models from a Code Security Perspective[C]// Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2025, 17349-17369. https://doi.org/10.18653/v1/2025.acl-long.849

[7] LIU F, LIU S, ZHU Y, et al. SecureReviewer: Enhancing Large Language Models for Secure Code Review through Secure-Aware Fine-Tuning[C]// Proceedings of the 2026 IEEE/ACM 48th International Conference on Software Engineering, 2026, 310-322. https://doi.org/10.1145/3744916.3773191

[8] ZHANG B, DU T, TONG J, et al. SecCoder: Towards Generalizable and Robust Secure Code Generation[C]// Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, 2024, 14557-14571. https://doi.org/10.18653/v1/2024.emnlp-main.806

[9] HASAN MS, CHAKRABORTY S, KARMAKER S, et al. Teaching an Old LLM Secure Coding: Localized Preference Optimization on Distilled Preferences[C]// Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2025, 26039-26057. https://doi.org/10.18653/v1/2025.acl-long.1263

[10] EL HUSSEINI A, IZZA Y, GENEST B, et al. Repairing LLM Executions for Secure Automatic Programming[C]// Proceedings of the 2026 IEEE/ACM 48th International Conference on Software Engineering, 2026, 818-829. https://doi.org/10.1145/3744916.3773210

[11] THANG M, WU L, BEHROUZI S, et al. GoodVibe: Security-by-Vibe for LLM-Based Code Generation[C]// 35th USENIX Security Symposium, 2026, 4425–4442. https://www.usenix.org/conference/usenixsecurity26/presentation/thang

[12] LIN B, WANG S, QIN Y, et al. Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection[C]// Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security, 2025, 3356-3370. https://doi.org/10.1145/3719027.3765049

[13] SUN T, SU J, GAO Y, et al. Securing Retrieval-Augmented Code Generation via Contextual Knowledge Injection: A Case for Embedded IoT Applications[C]// 35th USENIX Security Symposium, 2026, 771–790. https://www.usenix.org/conference/usenixsecurity26/presentation/sun-tong

[14] LIU F, LIU Y, SHI L, et al. Beyond Functional Correctness: Exploring Hallucinations in LLM-Generated Code[J]. IEEE Transactions on Software Engineering, 2026, 52(3): 1037-1055. https://doi.org/10.1109/TSE.2026.3657432

[15] ZHAO Y, WU M, HU X, et al. HFuzzer: Testing Large Language Models for Package Hallucinations via Phrase-based Fuzzing[C]// 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 2025, 2746-2758. https://doi.org/10.1109/ASE63991.2025.00225

[16] SCHREIBER M, TIPPE P. Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis of Public GitHub Repositories[C]// Information and Communications Security (ICICS 2025), LNCS 16219, 2026, 153-172. https://doi.org/10.1007/978-981-95-3537-8_9

[17] CHEN Y, CHENG W, XIAO Y, et al. Insecure Coding Preferences in Long-Term Memory: Security Risks for LLM-based Code Generation[J]. Proceedings of the ACM on Software Engineering, 2026, 3(ISSTA): 1809-1831. https://doi.org/10.1145/3832170

[18] AGHAKHANI H, DAI W, MANOEL A, et al. TrojanPuzzle: Covertly Poisoning Code-Suggestion Models[C]// 2024 IEEE Symposium on Security and Privacy (SP), 2024, 1122-1140. https://doi.org/10.1109/SP54263.2024.00140

[19] YAN S, WANG S, DUAN Y, et al. An LLM-Assisted Easy-to-Trigger Backdoor Attack on Code Completion Models: Injecting Disguised Vulnerabilities against Strong Detection[C]// 33rd USENIX Security Symposium, 2024, 1795–1812. https://www.usenix.org/conference/usenixsecurity24/presentation/yan

[20] RUBEL K, NOPPEL M, WRESSNEGGER C. Generalized Adversarial Code-Suggestions: Exploiting Contexts of LLM-based Code-Completion[C]// Proceedings of the 20th ACM Asia Conference on Computer and Communications Security, 2025, 358-374. https://doi.org/10.1145/3708821.3733870