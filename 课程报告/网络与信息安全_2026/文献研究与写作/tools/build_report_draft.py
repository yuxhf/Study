"""Build the full report draft from reviewed, source-backed writing parts."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / 'draft_parts'
OUT = ROOT / '第29题_课程报告完整初稿.md'
refs = json.loads((ROOT / 'sources/bibliography_verified.json').read_text())

def match(pattern, text, fallback=''):
    result = re.search(pattern, text)
    return result.group(1) if result else fallback

def reference(r):
    cr = r.get('crossref') or {}
    original = r['original_record']
    authors = '; '.join(' '.join(filter(None, [a.get('given'), a.get('family')])) for a in cr.get('author', []))
    authors = authors or match(r'作者：(.*?)。', original)
    venue = '; '.join(cr.get('container-title') or [])
    year = (cr.get('published', {}).get('date-parts') or [[None]])[0][0]
    venue = venue or match(r'发表：(.*?)；', original)
    year = year or match(r'(20\d\d)', venue)
    venue = re.sub(r'[，,]\s*20\d\d\s*$', '', venue)
    kind = 'J' if cr.get('type') == 'journal-article' else 'C'
    volume = cr.get('volume') or ''
    issue = cr.get('issue') or ''
    pages = cr.get('page') or match(r'书目位置：(.*?)。', original)
    if r['id'] == '14':
        venue = 'Information and Communications Security (ICICS 2025), LNCS 16219'
        year = 2026
    if r['id'] == '01':
        pages = 'Article 218, 1–34'
    issue_text = f'({issue})' if issue else ''
    location = (volume + issue_text + (': ' if volume else '') + pages).strip()
    url = 'https://doi.org/' + r['doi'] if r.get('doi') else r['url']
    return f'[{r["id"]}] {authors}. [{r["title"]}]({url})[{kind}]. {venue}, {year}' + (f', {location}' if location else '') + '.'

front = '''# 软件供应链中大模型代码生成（Copilot）的安全缺陷自动检测

网络与信息安全课程报告｜AI辅助完整初稿｜2026年11月17日

> 版本说明：本稿由主agent与三位子agent协作起草，依据本地已核论文证据整理，未经作者审定；没有独立复现原论文实验。原课程指南禁止AI直接生成综述主体，本稿的生成方式如实保留，不能将其宣称为作者独立完成的终稿。原文版本、数据冲突和引用边界另见[核查记录](完整初稿_核查记录.md)。

## 摘要

大模型生成代码的安全风险贯穿代码补全、依赖推荐、上下文检索与开发者采纳等环节，单纯检查代码可运行或扫描器无报警，难以充分说明输出可靠。本报告围绕二十篇候选研究，从真实项目实证、安全评价、生成期防护、依赖与记忆风险以及后门规避展开分析，并区分直接检测方法与改变生成行为的干预技术。跨论文比较表明，功能与安全分集评测、类别偏斜、判定器误差及成功定义差异，会限制安全分数的解释；检索增强也需区分类型判断、评论质量与版本适用性。报告据此讨论带漏报约束的误报过滤、版本与可达性约束下的证据验证，以及跨威胁的功能安全联合评价。这些方向属于待验证研究建议，尚无本项目实验结果。可信检测的核心在于保留可追溯证据、明确适用边界，并在同一输出上检验风险控制与功能效用。

**关键词：** 大模型代码生成；软件供应链；漏洞检测；误报过滤；检索增强生成；安全评价

'''

papers = '\n\n'.join((PARTS / name).read_text().strip() for name in [
    '论文剖析_01-07.md', '论文剖析_08-14.md', '论文剖析_15-20.md'
])
papers = papers.replace('](../core/', '](core/').replace('](../sources/', '](sources/')
report = '\n\n'.join([
    front.strip(),
    (PARTS / '选题综述.md').read_text().strip(),
    '## 第二部分：单篇论文深入剖析\n\n以下数值均沿用所述论文及版本，证据定位列明图表与页码；没有将跨论文百分数作为统一排行榜。',
    papers,
    (PARTS / '深度评述.md').read_text().strip(),
    '## 参考文献\n\n编号沿用阅读阶段，以便回查。正式出版信息与本次实际阅读版本的差别见核查记录；[14]按本地来源记录采用Springer推荐引文年份2026，其会议年份为2025。\n\n' + '\n\n'.join(reference(r) for r in refs),
]) + '\n'
OUT.write_text(report)

sections = re.findall(r'^### 2\.(\d+) \[(\d{2})\].*?\n(.*?)(?=^### 2\.|^## |\Z)', report.split('## 第二部分：')[1].split('## 第三部分：')[0], re.S | re.M)
counts = []
for n, rid, content in sections:
    paragraphs = [p for p in re.split(r'\n\s*\n', content.strip()) if p.strip() and not p.strip().startswith('证据定位')]
    body = '\n'.join(paragraphs)
    counts.append({'id': rid, 'section': int(n), 'han_characters': len(re.findall(r'[\u4e00-\u9fff]', body))})
stats = {'date': '2026-11-17', 'paper_sections': counts, 'total_characters': len(report), 'independent_replication': False, 'author_reviewed': False}
(ROOT / 'sources/report_draft_validation.json').write_text(json.dumps(stats, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(stats, ensure_ascii=False))
