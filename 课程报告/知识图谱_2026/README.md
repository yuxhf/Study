# 2026 年《知识图谱》课程报告

## 暂定选题（已根据要求调整）
**面向大语言模型的知识图谱构建、检索与推理技术研究**

副标题：**以 GraphRAG 与长期记忆为例**  
英文：*Knowledge Graph Construction, Retrieval, and Reasoning for Large Language Models: GraphRAG and Long-Term Memory as Applications*

### 明确范围
- **4 篇知识图谱核心研究 + 1 篇 Memory 研究**。重点放在知识图谱的构建、检索、子图提取与多跳推理。
- Memory **只保留 HippoRAG 2 一篇**，作为图谱增强 RAG 的延伸应用；不再以 Agent Memory 为综述主线。
- Complementary RL 可在最后的“结合本人研究”一段提及，但**既不计入 5 篇，也不专设 Memory 专章**。
- 《网络与信息安全》课程继续独立管理，互不强制关联。

## 课堂要求
1. **5 篇同主题 CCF A 类论文全文翻译**：英文标题保留，参考文献不翻译。
2. 对 5 篇论文进行对比分析。
3. 知识图谱结合本人科研方向提出新思路。
4. **2026-11-27（周五）**第 13 周最后一次课堂提交，纸质版、双面打印。

## 文件
- [报告框架.md](./报告框架.md)：以 KG 为中心的简要写作框架、待补充内容与比较矩阵。
- [文献清单.md](./文献清单.md)：4 KG + 1 Memory 的正式主会论文与原文入口。
- [原组会材料（选用 HippoRAG 2 相关页）](https://yuxhf.github.io/GroupMT/meetings/2026-11-08-agent-memory/index.html)。

## 进度
**已完成：选题框架调整、五篇主会文献的出版入口核验、课程目录材料更新。**  
**未完成：全文翻译、逐篇精读与图表复核、文献横向比较的最终论证、研究新思路的本人补充、印刷版制作。**

学术说明：KGP 构建的是跨文档段落/结构关系图，G-Retriever 面向一般文本属性图，二者不完全等同于传统实体—关系—实体三元组 KG；在报告中明确这一差异，作为 GraphRAG/图结构检索的重要扩展。
