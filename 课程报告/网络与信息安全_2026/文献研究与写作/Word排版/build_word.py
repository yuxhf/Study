from pathlib import Path
from copy import deepcopy
import re,json,hashlib
from docx import Document
from docx.shared import Cm,Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION_START
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT

ROOT=Path(__file__).resolve().parent
REFERENCE=Path('C:/Users/19252/Downloads/2026_网络与信息安全_研究生课程报告指南及前沿选题.docx')
OUT=ROOT/'1202621669_胡逢彬_网络与信息安全课程报告_审阅稿.docx'
source=(ROOT/'source.md').read_text(encoding='utf-8')
title=source.splitlines()[0].lstrip('# ')
body=source[source.index('## 摘要'):source.index('## 参考文献')]
refs_part=source[source.index('## 参考文献'):]
ref_matches=re.findall(r'^\[(\d{2})\]\s+(.+)$',refs_part,re.M)
refs=dict(ref_matches)
order=[]
for old in re.findall(r'\[(\d{2})\]',body):
 if old not in order:order.append(old)
assert len(order)==len(refs)==20
numbers={old:str(i+1) for i,old in enumerate(order)}
body=re.sub(r'\[(\d{2})\]',lambda m:'['+numbers[m[1]]+']',body)

def set_font(run,size=12,bold=False,cn='宋体'):
 run.font.name='Times New Roman';run.font.size=Pt(size);run.bold=bold;run.font.color.rgb=RGBColor(0,0,0)
 rpr=run._r.get_or_add_rPr();rf=rpr.rFonts
 if rf is None:rf=OxmlElement('w:rFonts');rpr.insert(0,rf)
 for k,v in [('eastAsia',cn),('ascii','Times New Roman'),('hAnsi','Times New Roman'),('cs','Times New Roman')]:rf.set(qn('w:'+k),v)
 for k in ['asciiTheme','hAnsiTheme','eastAsiaTheme','cstheme']:rf.attrib.pop(qn('w:'+k),None)

def link(p,text,url,size=10.5,bold=False):
 h=OxmlElement('w:hyperlink');h.set(qn('r:id'),p.part.relate_to(url,RT.HYPERLINK,is_external=True))
 r=OxmlElement('w:r');runpr=OxmlElement('w:rPr');rf=OxmlElement('w:rFonts');rf.set(qn('w:ascii'),'Times New Roman');rf.set(qn('w:hAnsi'),'Times New Roman');rf.set(qn('w:eastAsia'),'宋体');runpr.append(rf)
 co=OxmlElement('w:color');co.set(qn('w:val'),'000000');runpr.append(co)
 sz=OxmlElement('w:sz');sz.set(qn('w:val'),str(int(size*2)));runpr.append(sz)
 if bold:runpr.append(OxmlElement('w:b'))
 r.append(runpr);t=OxmlElement('w:t');t.text=text;r.append(t);h.append(r);p._p.append(h)

def rich(p,text,size=12,cn='宋体',bold=False):
 for chunk in re.split(r'(\*\*[^*]+\*\*|\[[^\]]+\]\([^)]+\))',text):
  if not chunk:continue
  m=re.fullmatch(r'\[([^\]]+)\]\(([^)]+)\)',chunk)
  if m:
   url=m[2] if m[2].startswith('http') else 'https://github.com/yuxhf/Study/blob/main/课程报告/网络与信息安全_2026/文献研究与写作/'+m[2]
   link(p,m[1],url,size,bold)
  else:set_font(p.add_run(chunk.strip('*').replace('`','')),size,bold or chunk.startswith('**'),cn)

doc=Document(REFERENCE)
original_parts={k:hashlib.sha256(v.blob).hexdigest() for k,v in [(str(p.partname),p) for p in doc.part.package.parts] if '/media/' in k}
children=list(doc.element.body)
cover=[deepcopy(x) for x in children[78:87]]
cover_section=deepcopy(doc.sections[0]._sectPr)
for e in list(doc.element.body):doc.element.body.remove(e)
for e in cover:doc.element.body.append(e)
doc.element.body.append(cover_section)
for sect in doc.sections:
 for footer in [sect.footer,sect.first_page_footer,sect.even_page_footer]:
  for p in footer.paragraphs:p.clear()
table=doc.tables[0]
values=['胡逢彬','1202621669','专业学位硕士','电子信息']
for row,value in zip(table.rows,values):
 p=row.cells[1].paragraphs[0];p.clear();set_font(p.add_run(value),14)
 p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.first_line_indent=Pt(0)
# 按用户提供的学院信息增加一行，复用原封面的单元格和边框样式。
college=deepcopy(table.rows[0]._tr);table._tbl.insert(4,college)
from docx.table import _Row
newrow=_Row(college,table)
for cell,value in zip(newrow.cells,['学      院','计算机与智能学院']):
 p=cell.paragraphs[0];p.clear();set_font(p.add_run(value),14);p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.first_line_indent=Pt(0)
for row in table.rows:
 for cell in row.cells:
  for p in cell.paragraphs:
   p.paragraph_format.first_line_indent=0;p.paragraph_format.left_indent=0;p.paragraph_format.right_indent=0
   ind=p._p.get_or_add_pPr().find(qn('w:ind'))
   if ind is not None:
    for attr in ['firstLineChars','leftChars','rightChars']:ind.attrib.pop(qn('w:'+attr),None)

def style(name,size,cn='宋体',bold=False,align=WD_ALIGN_PARAGRAPH.JUSTIFY,before=0,after=0,indent=24):
 s=doc.styles[name] if name in doc.styles else doc.styles.add_style(name,1)
 s.font.name='Times New Roman';s.font.size=Pt(size);s.font.bold=bold;s.font.color.rgb=RGBColor(0,0,0)
 rf=s.element.get_or_add_rPr().rFonts
 if rf is None:rf=OxmlElement('w:rFonts');s.element.get_or_add_rPr().insert(0,rf)
 rf.set(qn('w:eastAsia'),cn);rf.set(qn('w:ascii'),'Times New Roman');rf.set(qn('w:hAnsi'),'Times New Roman')
 for a in ['asciiTheme','hAnsiTheme','eastAsiaTheme','cstheme']:rf.attrib.pop(qn('w:'+a),None)
 f=s.paragraph_format;f.alignment=align;f.line_spacing=1.3;f.space_before=Pt(before);f.space_after=Pt(after);f.first_line_indent=Pt(indent)
 f.widow_control=True
 if name in ['Heading 1','Heading 2','Heading 3']:f.keep_with_next=True
 return s
style('Normal',12)
style('Title',16,'黑体',True,WD_ALIGN_PARAGRAPH.CENTER,0,18,0)
style('Heading 1',16,'黑体',True,WD_ALIGN_PARAGRAPH.CENTER,31.2,15.6,0)
style('Heading 2',14,'黑体',True,WD_ALIGN_PARAGRAPH.LEFT,15.6,7.8,0)
style('Heading 3',12,'黑体',True,WD_ALIGN_PARAGRAPH.LEFT,7.8,7.8,0)
style('FrontTitle',16,'黑体',True,WD_ALIGN_PARAGRAPH.CENTER,18,18,0)
style('Evidence',10.5,'宋体',False,WD_ALIGN_PARAGRAPH.LEFT,3,6,0)
style('Caption',10.5,'宋体',True,WD_ALIGN_PARAGRAPH.CENTER,8,5,0)
style('Bibliography',10.5,'宋体',False,WD_ALIGN_PARAGRAPH.JUSTIFY,0,4,0)
doc.styles['Bibliography'].paragraph_format.line_spacing=1.5
doc.styles['Bibliography'].paragraph_format.left_indent=Pt(21)
doc.styles['Bibliography'].paragraph_format.first_line_indent=Pt(-21)
style('ContentsEntry',12,'宋体',False,WD_ALIGN_PARAGRAPH.LEFT,6,6,0)
doc.styles['ContentsEntry'].paragraph_format.tab_stops.add_tab_stop(Cm(15.8),WD_ALIGN_PARAGRAPH.RIGHT)

def configure(sec,numbered=False):
 sec.page_width=Cm(21);sec.page_height=Cm(29.7);sec.top_margin=Cm(3);sec.bottom_margin=Cm(2.5);sec.left_margin=Cm(2.5);sec.right_margin=Cm(2.5)
 sec.header_distance=Cm(1.2);sec.footer_distance=Cm(1.3);sec.gutter=0
 sec.header.is_linked_to_previous=False;sec.footer.is_linked_to_previous=False
 for h in [sec.header,sec.footer]:
  for p in h.paragraphs:p.clear()
 sec.different_first_page_header_footer=False
 for el in sec._sectPr.findall(qn('w:pgNumType')):sec._sectPr.remove(el)
 if numbered:
  num=OxmlElement('w:pgNumType');num.set(qn('w:start'),'1');num.set(qn('w:fmt'),'decimal');sec._sectPr.append(num)
  p=sec.footer.paragraphs[0];p.alignment=WD_ALIGN_PARAGRAPH.CENTER
  p.paragraph_format.first_line_indent=0
  r=p.add_run();set_font(r,9)
  begin=OxmlElement('w:fldChar');begin.set(qn('w:fldCharType'),'begin');r._r.append(begin)
  ins=OxmlElement('w:instrText');ins.text=' PAGE ';r._r.append(ins)
  sep=OxmlElement('w:fldChar');sep.set(qn('w:fldCharType'),'separate');r._r.append(sep)
  t=OxmlElement('w:t');t.text='1';r._r.append(t)
  end=OxmlElement('w:fldChar');end.set(qn('w:fldCharType'),'end');r._r.append(end)

sec=doc.add_section(WD_SECTION_START.NEW_PAGE);configure(sec)
p=doc.add_paragraph(style='Title');rich(p,title,16,'黑体',True)
p=doc.add_paragraph(style='Evidence');rich(p,'审阅稿说明：本稿由已有AI辅助初稿排版，尚未经作者逐项审定，也未独立复现原论文实验。依课程指南，主体内容仍需本人核对与二次重构后再提交。',10.5)
abstract,main=body.split('## 第一部分',1)
abstract_lines=abstract.splitlines()
doc.add_paragraph('摘要','FrontTitle')
for line in abstract_lines[1:]:
 if line.strip():rich(doc.add_paragraph(),line.strip())
doc.add_page_break();doc.add_paragraph('目录','FrontTitle')
toc=[]
toc_pages=json.loads((ROOT/'toc_pages.json').read_text(encoding='utf-8')) if (ROOT/'toc_pages.json').exists() else [1,2,16,20]
for i,text in enumerate(['第一部分 选题依据与文献分类综述','第二部分 单篇论文深入剖析','第三部分 整体深度综述与前沿展望','参考文献']):
 p=doc.add_paragraph(style='ContentsEntry');p.paragraph_format.tab_stops.clear_all()
 from docx.enum.text import WD_TAB_ALIGNMENT,WD_TAB_LEADER
 p.paragraph_format.tab_stops.add_tab_stop(Cm(15.6),WD_TAB_ALIGNMENT.RIGHT,WD_TAB_LEADER.DOTS)
 rich(p,text+'\t'+str(toc_pages[i]));p._p.set(qn('w:rsidR'),'7777000'+str(i));toc.append(p)
begin_run=OxmlElement('w:r');bf=OxmlElement('w:fldChar');bf.set(qn('w:fldCharType'),'begin');begin_run.append(bf)
inst=OxmlElement('w:r');it=OxmlElement('w:instrText');it.set(qn('xml:space'),'preserve');it.text=' TOC \\o "1-1" \\h \\z \\u ';inst.append(it)
separator=OxmlElement('w:r');sf=OxmlElement('w:fldChar');sf.set(qn('w:fldCharType'),'separate');separator.append(sf)
for element in [separator,inst,begin_run]:toc[0]._p.insert(1,element)
end_run=OxmlElement('w:r');ef=OxmlElement('w:fldChar');ef.set(qn('w:fldCharType'),'end');end_run.append(ef);toc[-1]._p.append(end_run)

sec=doc.add_section(WD_SECTION_START.NEW_PAGE);configure(sec,True)
main='## 第一部分'+main
lines=main.splitlines();i=0;partno=0;section_titles=[]
while i<len(lines):
 s=lines[i].strip()
 if not s:i+=1;continue
 if s.startswith('## '):
  text=s[3:].replace('：',' ',1);partno+=1
  p=doc.add_paragraph(style='Heading 1');p.paragraph_format.page_break_before=partno>1;rich(p,text,16,'黑体',True);section_titles.append(text);i+=1;continue
 if s.startswith('### '):
  p=doc.add_paragraph(style='Heading 2');rich(p,s[4:],14,'黑体',True);i+=1;continue
 if s.startswith('|'):
  rows=[]
  while i<len(lines) and lines[i].strip().startswith('|'):
   cells=[v.strip() for v in lines[i].strip().strip('|').split('|')]
   if not all(re.fullmatch(r':?-{2,}:?',c) for c in cells):rows.append(cells)
   i+=1
  rich(doc.add_paragraph(),'表3-1汇总各类检测与防护路线的输出、适用条件以及验收所需证据。')
  doc.add_paragraph('表3-1 安全缺陷检测与防护路线比较','Caption')
  t=doc.add_table(rows=0,cols=len(rows[0]));t.autofit=False
  widths=[3.3,2.8,4.2,5.7]
  for rr,row in enumerate(rows):
   cells=t.add_row().cells
   for c,v,w in zip(cells,row,widths):
    c.width=Cm(w);p=c.paragraphs[0];p.paragraph_format.first_line_indent=0;p.paragraph_format.line_spacing=1.3;p.paragraph_format.space_after=Pt(3);rich(p,v,10.5,bold=rr==0)
    tcPr=c._tc.get_or_add_tcPr();marg=OxmlElement('w:tcMar')
    for side in ['top','bottom','left','right']:
     e=OxmlElement('w:'+side);e.set(qn('w:w'),'80');e.set(qn('w:type'),'dxa');marg.append(e)
    tcPr.append(marg)
   trPr=t.rows[-1]._tr.get_or_add_trPr();trPr.append(OxmlElement('w:cantSplit'))
   if rr==0:trPr.append(OxmlElement('w:tblHeader'))
  for col,w in zip(t.columns,widths):col.width=Cm(w)
  borders=OxmlElement('w:tblBorders')
  for side in ['top','bottom','insideH','left','right','insideV']:
   b=OxmlElement('w:'+side);b.set(qn('w:val'),'single' if side in ['top','bottom'] else 'nil');b.set(qn('w:sz'),'8');b.set(qn('w:color'),'000000');borders.append(b)
  t._tbl.tblPr.append(borders)
  for c in t.rows[0].cells:
   bs=OxmlElement('w:tcBorders');bb=OxmlElement('w:bottom');bb.set(qn('w:val'),'single');bb.set(qn('w:sz'),'4');bs.append(bb);c._tc.get_or_add_tcPr().append(bs)
  continue
 is_evidence=s.startswith(('证据','**证据','来源','**来源'))
 p=doc.add_paragraph(style='Evidence' if is_evidence else 'Normal');rich(p,s,10.5 if is_evidence else 12);i+=1

p=doc.add_paragraph('参考文献','Heading 1');p.paragraph_format.page_break_before=True
def gb_author(a):
 words=a.strip().split()
 if a.endswith('El Husseini'):return 'EL HUSSEINI '+''.join(w[0].upper() for w in words[:-2])
 return words[-1].upper()+' '+''.join(w[0].upper() for w in words[:-1])
formatted=[]
for old in order:
 text=refs[old];m=re.match(r'(.+?)\. \[([^\]]+)\]\(([^)]+)\)\[([JC])\]\. (.+)',text)
 assert m,(old,text)
 authors,ptitle,url,kind,venue=m.groups();people=[a.strip() for a in authors.split(';')]
 names=', '.join(gb_author(a) for a in people[:3])+(', et al.' if len(people)>3 else '')
 entry='['+numbers[old]+'] '+names.rstrip('.')+'. '+ptitle+'['+kind+']'+('// ' if kind=='C' else '. ')+venue
 p=doc.add_paragraph(style='Bibliography');rich(p,entry,10.5)
 rich(p,' DOI: '+url.removeprefix('https://doi.org/') if 'doi.org/' in url else ' '+url,10.5)
 formatted.append(entry+' '+url)

settings=doc.settings.element
u=settings.find(qn('w:updateFields'))
if u is None:u=OxmlElement('w:updateFields');settings.append(u)
u.set(qn('w:val'),'true')
# 使用精确字符缩进，避免因中文西文字体混排改变首行距离。
for p in doc.paragraphs:
 if p.style.name=='Normal':
  ind=p._p.get_or_add_pPr().find(qn('w:ind'))
  if ind is not None:ind.set(qn('w:firstLineChars'),'200')
  snap=OxmlElement('w:snapToGrid');snap.set(qn('w:val'),'0');p._p.get_or_add_pPr().append(snap)
doc.core_properties.title=title;doc.core_properties.author='胡逢彬';doc.core_properties.subject='网络与信息安全课程报告审阅稿'
doc.save(OUT)
final=Document(OUT)
for part in final.part.package.parts:
 key=str(part.partname)
 if key in original_parts:assert hashlib.sha256(part.blob).hexdigest()==original_parts[key]
(ROOT/'citation_mapping.json').write_text(json.dumps(numbers,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'formatted_source.md').write_text('# '+title+'\n\n> 审阅稿：保留AI辅助初稿来源，需本人核对与主体二次重构。\n\n'+body+'\n\n## 参考文献\n\n'+'\n\n'.join(formatted),encoding='utf-8')
(ROOT/'build_manifest.json').write_text(json.dumps(dict(output=OUT.name,reference_sha256=hashlib.sha256(REFERENCE.read_bytes()).hexdigest(),source_sha256=hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),references=len(refs),citation_mapping=numbers,identity=dict(name='胡逢彬',student_id='1202621669',college='计算机与智能学院',major='电子信息',degree='专业学位硕士'),body_line_spacing=1.3,body_first_line_characters=2,paper='A4',margins_cm=dict(top=3,bottom=2.5,left=2.5,right=2.5)),ensure_ascii=False,indent=2),encoding='utf-8')
print(OUT)
