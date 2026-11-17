from pathlib import Path
b=Path('E:/GroupMT/study-report/课程报告/知识图谱_2026/翻译源稿')
p=b/'04_FastToG.md';s=p.read_text(encoding='utf8')
x='''
图1图内文字补译。问题：“如果春天前往宾夕法尼亚会议中心附近地区，我应该带什么衣服？”a：寻找与Pennsylvania Convention Center相关三元组；Retrieve=检索，Answer=回答，Prompt=提示；cloth衣物关系“不存在”；提示“宾夕法尼亚会议中心位于Market East Section；未找到Market East Section的衣物信息”；回复“抱歉，根据知识库查询结果，我无法回答，因为信息不足。”b：提取该中心所有深度d=2的邻居关系r与实体e；Retrieve Nodes=检索节点；图节点Wilson Brothers & Company、Renovated by=改建方；提示“中心位于Market East Section，由Wilson Brothers & Company改建；中心位于……”，回复同样表示信息不足。c：寻找中心相关三元组，检索节点，思考“最相关的是（……）；信息不足，寻找与Market East Section相关三元组”；再次思考“最相关的是（……）；信息不足，寻找与Pennsylvania相关三元组”；过多思考后获得Enough Information=足够信息。链为中心—isLocatedIn位于→Market East Section—isLocatedIn位于→…—isCityOf所属城市→Pennsylvania—climate气候→humid subtropical湿润亚热带。d：检索社区，将宾夕法尼亚州社区整体作为证据，思考“最相关的是（Pennsylvania Convention Center,isLocatedIn,Pennsylvania State）；信息不足，寻找与宾夕法尼亚州社区相关的社区”，以更少思考获得足够信息。两种成功回答均为“春季湿润亚热带地区建议穿轻便透气衣物。因此，若前往宾夕法尼亚会议中心，可考虑棉衬衫、短裤和连衣裙。”Combine=结合；LLMs inner knowledge=LLM内部知识，其内容为“气温从凉爽到温和，降雨增加，湿度较高”。Think=思考，answer=回答；Community: Pennsylvania State=宾夕法尼亚州社区。

'''
s=s.replace('![图1 原图',x+'![图1 原图',1)
x='''图2图内标签：Community Detection on Subgraph=子图社区检测；Start/Header Community=起始／首社区；Start=起点；Modularity based Coarse-pruning=基于模块度的粗剪枝；low modularity=低模块度；LLMs based Fine-pruning=基于LLM的精剪枝；Reasoning=推理；Yes,the answer is…=是，答案为……；No,restart from this=否，从此处重新开始。Q(c)保留原符号。

'''
s=s.replace('![图2 FastToG',x+'![图2 FastToG',1)
s=s.replace('图3：平均深度与社区最大大小。','图3至图5图内标签：Avg Depth=平均深度，Max Size=最大大小，Accuracy (%)=准确率（%），t2t/g2t为两种社区文本模式；Modularity-based Pruning=模块度剪枝，Random Pruning=随机剪枝。图3：平均深度与社区最大大小。')
s=s.replace('![图6检索可视化', '''图6图内标签：Community=社区（编号0—3）；Community with potential answer=含潜在答案的社区；Community with answer=含答案的社区；Central America=中美洲；El Salvador=萨尔瓦多；Sonsonate Department=松索纳特省；Izalco=伊萨尔科；Cordillera de Apaneca-Lamatepec=阿帕内卡—拉马特佩克山脉；Spanish=西班牙语；historical period=历史时期；The Nuttall Encyclopædia=Nuttall百科全书；Category:1960s=分类：1960年代；Category:Shia Islam…=分类：什叶派伊斯兰教……；A new species of Phrynus Lamarck,…=Phrynus Lamarck的一种新物种……；Carlos Víquez=原图人名；Las de Abajo=原图作品名；First record of the genus Piarpa…=Piarpa属首次记录……（按图中字样）；Nueva especie de Phrynus (Amblypygi:…)=Phrynus新物种（无尾鞭蝎目：……）；Revista Ibérica de Aracnología…=伊比利亚蛛形学期刊……。原图部分节点标签带省略号，译文同样保留省略边界。

![图6检索可视化''',1)
p.write_text(s,encoding='utf8')
p=b/'05_HippoRAG2.md';s=p.read_text(encoding='utf8')
s=s.replace('![图1原图]', '''图1图内逐项翻译：Factual Memory=事实记忆，问题“George Rankin的职业是什么？”；错误候选“Oliver Badman是政治家”“Thomas Marwick是政治家”，正确候选“George Rankin是政治家”。Sense-making=意义建构，问题“灰姑娘如何获得幸福结局？”；顺序为“灰姑娘参加皇家舞会”“王子用遗失的玻璃鞋搜寻整个王国”“鞋子完全合脚时，灰姑娘与王子重聚”。Associativity=关联性，问题“Erik Hort的出生地属于哪个县？”；正确事实“其出生地为Montebello”“Montebello属于Rockland County”，干扰事实“Marina出生在Minsk”；Associated=已关联。下方各柱依次为RAPTOR、GraphRAG、HippoRAG、NV-Embed-v2、HippoRAG 2，均为方法名。事实记忆值53.45、47.50、55.60、58.80、59.75；意义建构21.40、23.00、16.30、25.70、25.90；关联性48.37、53.49、54.88、58.81、62.96。

![图1原图]''',1)
s=s.replace('![图2原图]', '''图2其他文字：Offline Indexing=离线索引；Passages=文段；Triples=三元组；Knowledge Graph=知识图谱；1 OpenIE by LLM=LLM进行开放信息抽取；2 Synonym detection by embedding=以嵌入检测同义；3 Dense-sparse integration=稠密稀疏整合。Online Retrieval & QA=在线检索和问答；Query=查询；Ranked Passages=已排序文段；Ranked Triples=已排序三元组；Filtered triples=筛选后三元组；Answer=答案；在线步骤1检索文段和三元组，2识别记忆（三元组筛选），3分配种子节点权重，4 PPR图搜索，5以所选文段完成问答阅读。

![图2原图]''',1)
p.write_text(s,encoding='utf8')
