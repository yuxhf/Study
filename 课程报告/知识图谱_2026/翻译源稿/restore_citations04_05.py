from pathlib import Path
b=Path('E:/GroupMT/study-report/课程报告/知识图谱_2026/翻译源稿')
p=b/'04_FastToG.md';s=p.read_text(encoding='utf8')
pairs=[
('早期的朴素RAG通常','早期的朴素RAG（Gao等，2023）通常'),
('向量相似度检索相关上下文','向量相似度（Karpukhin等，2020）检索相关上下文'),
('广泛用于问答、推荐和对话系统','广泛用于问答（Chan等，2024）、推荐系统（Deldjoo等，2024）和对话系统（Ni等，2023）'),
('嵌入模型中的歧义或偏差会降低','嵌入模型中的歧义或偏差（Thurnbauer等，2023）会降低'),
('GRAG支持广度优先搜索','GRAG支持复杂操作（Liang等，2024），例如广度优先搜索'),
('仍有不少工作采用1-w 1-d图RAG','仍有不少工作（Andrus等，2022；Baek、Aji和Saffari，2023；Li等，2023）采用1-w 1-d图RAG'),
('n-w GRAG旨在扩大检索上下文窗口','n-w GRAG研究（Jiang等，2023；Modarressi等，2023；Edge等，2024；Wang等，2024）旨在扩大检索上下文窗口'),
('n-d GRAG通过增加上下文深度','n-d GRAG（Sun等，2023；Wang等，2022a）通过增加上下文深度'),
('类似“让我们逐步思考”','类似“让我们逐步思考”（Kojima等，2022）'),
('Louvain和Leiden使用模块度','Louvain（Blondel等，2008）和Leiden（Traag、Waltman和Van Eck，2019）使用模块度'),
('Girvan–Newman（GN）算法','Girvan–Newman（GN）算法（Girvan和Newman，2002）'),
('Xie等将图线性化后','Xie等（2022）将图线性化后'),
('Zhang等借助知识编码器','Zhang等（2019）借助知识编码器'),
('K-Adapter通过Transformer适配器','Wang等（2020）的K-Adapter通过Transformer适配器'),
('LUKE增强实体感知','Yamada等（2020）的LUKE增强实体感知'),
('1-w 1-d包括CoK和KAPING','1-w 1-d包括CoK（Li等，2023）和KAPING（Baek、Aji和Saffari，2023）'),
('n-w代表包括KGP、StructGPT、RET-LLMs和GraphRAG','n-w代表包括KGP（Wang等，2024）、StructGPT（Jiang等，2023）、RET-LLMs（Modarressi等，2023）和GraphRAG（Edge等，2024）'),
('n-d代表包括KP-PLM和ToG','n-d代表包括KP-PLM（Wang等，2022a）和ToG（Sun等，2023）'),
('受“让我们逐步思考”启发','受“让我们逐步思考”（Kojima等，2022）启发'),
('本文考虑Louvain、GN、凝聚层次聚类和谱聚类','本文考虑Louvain（Blondel等，2008）、GN（Girvan和Newman，2002）、凝聚层次聚类和谱聚类'),
('耗时长或产生选择偏差','耗时长或产生选择偏差（Zheng等，2023）'),
('分区子图的模块度为','分区子图的模块度（Blondel等，2008）为'),
('不再让LLM打分','不再采用基于评分的剪枝（Sun等，2023），不再让LLM打分'),
('与ToG一致，初始阶段','与ToG（Sun等，2023）一致，初始阶段'),
('多跳知识库问答CWQ、WebQSP、QALD；槽填充ZSRE和TREx；常识推理Creak','多跳知识库问答CWQ（Talmor和Berant，2018）、WebQSP（Yih等，2016）、QALD（Perevalov等，2022）；槽填充ZSRE（Petroni等，2021）和TREx（Elsahar等，2018）；常识推理Creak（Onoe等，2021）'),
('为与先前工作一致，采用','为与先前工作（Li等，2023；Sun等，2023；Edge等，2024）一致，采用'),
('起始社区采用Sun等提供','起始社区采用Sun等（2023）提供'),
('无量化Llama-3-70B-Instruct','无量化Llama-3-70B-Instruct（Dubey等，2024）'),
('G2T通过WebNLG和GPT-4生成的合成数据微调T5-base实现','G2T通过WebNLG（Auer等，2007）和GPT-4生成的合成数据微调T5-base（Raffel等，2020）实现'),
('采用2024-01-01版Wikidata','采用2024-01-01版Wikidata（Vrandečić和Krötzsch，2014）'),
('直接输出IO、逐步思考CoT以及集成多个思维链得到一致预测的CoT-SC','直接输出IO（Brown等，2020）、逐步思考CoT（Wei等，2022）以及集成多个思维链得到一致预测的CoT-SC（Wang等，2022b）'),
('代表CoK、KAPING的1-d 1-w，代表KGP的1-d n-w，以及代表ToG的n-d 1-w','代表CoK（Li等，2023）、KAPING（Baek、Aji和Saffari，2023）的1-d 1-w，代表KGP（Wang等，2024）的1-d n-w，以及代表ToG（Sun等，2023）的n-d 1-w')
]
miss=[]
for old,new in pairs:
 if old not in s:miss.append(old)
 else:s=s.replace(old,new,1)
p.write_text(s,encoding='utf8');print('04 unmatched',miss)
p=b/'05_HippoRAG2.md';s=p.read_text(encoding='utf8')
pairs=[
('既难以完整吸收新知识，也难避免灾难性遗忘','既难以完整吸收新知识（Zhong等，2023；Hoelscher-Obermaier等，2023），也难避免灾难性遗忘（Cohen等，2024；Gu等，2024）'),
('凭借简单、稳健的特点','凭借简单、稳健的特点（Zhong等，2023；Xie等，2024）'),
('意义建构，即解释更大、更复杂或不确定上下文的能力；关联性，即在分散知识之间建立多跳联系的能力','意义建构（Klein等，2006），即解释更大、更复杂或不确定上下文的能力；关联性（Suzuki，2005），即在分散知识之间建立多跳联系的能力'),
('让LLM生成摘要或知识图谱','让LLM生成摘要（Edge等，2024；Sarthi等，2024；Chen等，2023）或知识图谱（Guo等，2024）'),
('HippoRAG使用个性化PageRank和LLM','HippoRAG（Gutiérrez等，2024）使用个性化PageRank（Haveliwala，2002）和LLM'),
('多个基准工作已体现这一需求','多个基准工作（Zhong等，2023；Liska等，2022；Kim等，2024；Roth等，2024；Li等，2024）已体现这一需求'),
('通常分为持续微调、模型编辑和RAG','通常分为持续微调、模型编辑和RAG（Shi等，2024）'),
('可采用持续预训练、指令微调和对齐微调','可采用持续预训练（Jin等，2022）、指令微调（Zhang等，2023）和对齐微调（Zhang等，2024）'),
('但存在灾难性遗忘，即','但存在灾难性遗忘（Huang等，2024），即'),
('模型编辑通过直接修改特定参数','模型编辑（Yao等，2023）通过直接修改特定参数'),
('近期模型借助LLM、大语料','近期模型（Li等，2023；Muennighoff等，2025；Lee等，2025）借助LLM、大语料'),
('本文以NV-Embed-v2为主要比较对象','本文以NV-Embed-v2（Lee等，2025）为主要比较对象'),
('意义建构是理解大规模或复杂事件、经历、数据的能力','意义建构是理解大规模或复杂事件、经历、数据的能力（Koli等，2024）'),
('RAPTOR和GraphRAG均生成整合语料的摘要','RAPTOR（Sarthi等，2024）和GraphRAG（Edge等，2024）均生成整合语料的摘要'),
('LightRAG结合图结构和向量检索','LightRAG（Guo等，2024）结合图结构和向量检索'),
('HippoRAG通过显式开放KG上的PPR处理这一性质','HippoRAG（Gutiérrez等，2024）通过显式开放KG上的PPR处理这一性质'),
('HippoRAG为受神经生物学启发','HippoRAG（Gutiérrez等，2024）为受神经生物学启发'),
('HippoRAG 2沿用离线索引和在线检索两阶段','HippoRAG 2基于HippoRAG（Gutiérrez等，2024）的神经生物学记忆框架，沿用离线索引和在线检索两阶段'),
('稠密和稀疏编码理论解释大脑','稠密和稀疏编码理论（Beyeler等，2019）解释大脑'),
('许多信号未被利用','许多信号未被利用（Gutiérrez等，2024）'),
('回忆与识别是人类检索记忆的互补过程','回忆与识别是人类检索记忆的互补过程（Uner和Roediger III，2022）'),
('简单检索BM25、Contriever、GTR；BEIR表现强的7B大嵌入模型GTE-Qwen2-7B-Instruct、GritLM-7B、NV-Embed-v2；四种结构增强方法RAPTOR（语义层次结构）、GraphRAG和LightRAG（KG及高层摘要）、HippoRAG（KG与PPR整合，而非摘要）','简单检索BM25（Robertson和Walker，1994）、Contriever（Izacard等，2022）、GTR（Ni等，2022）；BEIR榜单（Thakur等，2021）表现强的7B大嵌入模型GTE-Qwen2-7B-Instruct（Li等，2023）、GritLM-7B（Muennighoff等，2025）、NV-Embed-v2（Lee等，2025）；四种结构增强方法RAPTOR（Sarthi等，2024；语义层次结构）、GraphRAG（Edge等，2024）和LightRAG（Guo等，2024）（KG及高层摘要）、HippoRAG（Gutiérrez等，2024；KG与PPR整合，而非摘要）'),
('从NaturalQuestions（NQ）随机取1000条','从NaturalQuestions（NQ；Wang等，2024收集）随机取1000条'),
('PopQA取1000条','PopQA（Mallen等，2023）取1000条'),
('遵循HippoRAG，从MuSiQue','遵循HippoRAG（Gutiérrez等，2024），从MuSiQue'),
('LV-Eval的hotpotwikiqa-mixup 256k','LV-Eval（Yuan等，2024）的hotpotwikiqa-mixup 256k'),
('遵循HippoRAG，以文段recall@5评价检索；遵循MuSiQue指标','遵循HippoRAG（Gutiérrez等，2024），以文段recall@5评价检索；遵循MuSiQue（Trivedi等，2022）指标'),
('以开源Llama-3.3-70B-Instruct完成NER','以开源Llama-3.3-70B-Instruct（AI@Meta，2024）完成NER'),
('通过DSPy MIPROv2','通过DSPy（Khattab等，2024）MIPROv2'),
('以vLLM张量并行运行','以vLLM（Kwon等，2023）张量并行运行'),
('并比较NV-Embed-v2、RAPTOR、LightRAG、HippoRAG、GraphRAG（表12）','并比较NV-Embed-v2（Lee等，2025）、RAPTOR（Sarthi等，2024）、LightRAG（Guo等，2024）、HippoRAG（Gutiérrez等，2024）、GraphRAG（Edge等，2024）（表12）'),
('稠密检索使用PyTorch和HuggingFace，BM25使用BM25s','稠密检索使用PyTorch（Paszke等，2019）和HuggingFace（Wolf等，2019），BM25使用BM25s（Lù，2024）'),
('GraphRAG与LightRAG遵循默认超参数和提示','GraphRAG（Edge等，2024）与LightRAG（Guo等，2024）遵循默认超参数和提示'),
('从HippoRAG继承的同一QA提示','从HippoRAG（Gutiérrez等，2024）继承的同一QA提示')
]
miss=[]
for old,new in pairs:
 if old not in s:miss.append(old)
 else:s=s.replace(old,new,1)
# Restore citations on translated rows of original Tables 2 and 3.
rowrefs={'Contriever':'Izacard等，2022','BM25':'Robertson和Walker，1994','GTR':'Ni等，2022','GTE-Qwen2':'Li等，2023','GritLM':'Muennighoff等，2025','NV-Embed-v2':'Lee等，2025','RAPTOR':'Sarthi等，2024','GraphRAG':'Edge等，2024','LightRAG':'Guo等，2024','HippoRAG':'Gutiérrez等，2024','HippoRAG原报告*':'Gutiérrez等，2024'}
for label,ref in rowrefs.items():s=s.replace('|'+label+'|','|'+label+'（'+ref+'）|')
p.write_text(s,encoding='utf8');print('05 unmatched',miss)
