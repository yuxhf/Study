from pathlib import Path
import re,html,json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,Image,KeepTogether,Flowable
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader,PdfWriter,Transformation
import pypdfium2 as pdfium
root=Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(TTFont('CN','C:/Windows/Fonts/simsun.ttc',subfontIndex=0))
pdfmetrics.registerFont(TTFont('Hei','C:/Windows/Fonts/simhei.ttf'))
pdfmetrics.registerFont(TTFont('Math','C:/Windows/Fonts/cambria.ttc',subfontIndex=0))
base=dict(fontName='CN',fontSize=10.5,leading=17,wordWrap='CJK',spaceAfter=6)
styles={
 'p':ParagraphStyle('p',**base),
 'h1':ParagraphStyle('h1',fontName='Hei',fontSize=20,leading=29,wordWrap='CJK',spaceBefore=12,spaceAfter=16,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='Hei',fontSize=15,leading=23,wordWrap='CJK',spaceBefore=15,spaceAfter=9,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='Hei',fontSize=12,leading=19,wordWrap='CJK',spaceBefore=11,spaceAfter=7,keepWithNext=True),
 'cell':ParagraphStyle('cell',fontName='CN',fontSize=8.5,leading=13,wordWrap='CJK'),
 'small':ParagraphStyle('small',fontName='CN',fontSize=8,leading=12,wordWrap='CJK',textColor=colors.HexColor('#555555'))}
W,H=A4;CW=W-102
placements=[]
class OriginalPage(Flowable):
 def __init__(self,source,index,width,height):
  Flowable.__init__(self);self.source=source;self.index=index;self.width=width;self.height=height
 def draw(self):
  x,y=self.canv.absolutePosition(0,0)
  placements.append((self.canv.getPageNumber()-1,self.source,self.index,x,y,self.width,self.height))
def glyph_fix(s):
 parts=re.split('(<[^>]+>)',s)
 for i in range(0,len(parts),2):
  parts[i]=''.join(('<font name="Math">'+c+'</font>') if ord(c) not in pdfmetrics.getFont('CN').face.charToGlyph and ord(c) in pdfmetrics.getFont('Math').face.charToGlyph else c for c in parts[i])
 return ''.join(parts)
def inline(s):
 s=re.sub(r'\\(?:mathrm|operatorname)\*?\{([^{}]*)\}',r'\1',s)
 s=html.escape(s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'`([^`]+)`',r'\1',s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1',s)
 # 行内数学变量保留为可读符号；显示公式优先使用核对后的富文本。
 s=s.replace('$$','').replace('$','')
 mappings={'\\theta':'θ','\\phi':'φ','\\gamma':'γ','\\alpha':'α','\\beta':'β','\\in':'∈','\\mathbb R':'ℝ','\\mid':' | ','\\prod':'Π','\\sum':'Σ','\\times':'×','\\cos':'cos','\\cdot':'·','\\quad':'  ','\\subseteq':'⊆','\\subset':'⊂','\\hat h':'ĥ','\\hat d':'d̂','\\text':'','\\operatorname':'','\\mathrm':'','\\mathop':'','\\leftarrow':'←','\\left':'','\\right':'','\\cup':'∪','\\Vert':'‖','\\mathcal N':'N','\\(':'','\\)':'','\\{':'{','\\}':'}'}
 for a,b in mappings.items():s=s.replace(a,b)
 return glyph_fix(s)
def para(s,kind='p'):return Paragraph(inline(s),styles[kind])
def footer(c,d):
 c.saveState();c.setFont('CN',8);c.setFillColor(colors.HexColor('#666666'))
 c.drawString(51,27,'知识图谱课程报告 · 2026');c.drawRightString(W-51,27,str(d.page));c.restoreState()
def markdown_flow(path):
 lines=path.read_text(encoding='utf-8-sig').splitlines();story=[];i=0;buf=[]
 def flush():
  if buf:story.append(para(' '.join(buf)));buf.clear()
 while i<len(lines):
  s=lines[i].strip()
  if not s:flush();i+=1;continue
  if s.startswith('<!--'):flush();i+=1;continue
  if 'DomainSpecificity}=\\frac' in s:
   flush();story.append(Paragraph(glyph_fix('DomainSpecificity = |T<sub>generated,domain,correct</sub> ∖ T<sub>openKG</sub>| / |T<sub>generated</sub>|'),styles['p']));i+=1;continue
  if s.startswith('s_{j+1}='):
   flush();story.append(Paragraph('s<sub>j+1</sub> = argmax<sub>v∈N_j</sub> φ(g(X<sub>v</sub>), f(‖<sub>k=0</sub><sup>j</sup> X<sub>k</sub>))　(1)',styles['p']));i+=1;continue
  if s.startswith('$$'):
   flush();m=re.search(r'\\tag\{(\d+)\}',s);eq=root/'构建与核验'/'equations_gretriever.json'
   if m and eq.exists():
    mapping=json.loads(eq.read_text(encoding='utf-8'))
    if m[1] in mapping:story.append(Paragraph(glyph_fix(mapping[m[1]]+'　('+m[1]+')'),styles['p']));i+=1;continue
  m=re.match(r'!\[(.*?)\]\((.*?)\)',s)
  if m:
   flush();p=path.parent/m[2]
   if p.exists():
    im=Image(str(p));ratio=min(CW/im.imageWidth,650/im.imageHeight)
    im.drawWidth=im.imageWidth*ratio;im.drawHeight=im.imageHeight*ratio
    original=re.search(r'assets[/\\](0[1-5])[/\\]page-(\d+)\.png',m[2])
    if original:
     source=next((root/'原文PDF').glob(original[1]+'_*.pdf'))
     im=OriginalPage(source,int(original[2])-1,im.drawWidth,im.drawHeight)
    story.extend([Spacer(1,5),im,para(m[1],'small'),Spacer(1,8)])
   else: raise FileNotFoundError(p)
   i+=1;continue
  if s.startswith('|'):
   flush();rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch(r':?-{2,}:?',x or '-') for x in cells):rows.append(cells)
    i+=1
   n=max(map(len,rows));data=[[para(x,'cell') for x in r]+['']*(n-len(r)) for r in rows]
   widths=[CW/n]*n
   if n==2:widths=[CW*.25,CW*.75]
   if n==3:widths=[CW*.22,CW*.26,CW*.52]
   table=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
   table.setStyle(TableStyle([('GRID',(0,0),(-1,-1),.4,colors.HexColor('#D9D9D9')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E9EDF0')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
   story.extend([Spacer(1,5),table,Spacer(1,10)]);continue
  if s.startswith('#'):
   flush();level=len(s)-len(s.lstrip('#'));story.append(para(s.lstrip('#').strip(),'h'+str(min(level,3))));i+=1;continue
  if s.startswith('```'):
   flush();i+=1
   while i<len(lines) and not lines[i].startswith('```'):
    story.append(para(lines[i],'small'));i+=1
   i+=1;continue
  if s in ['---','***']:flush();i+=1;continue
  if re.match(r'^([-*]|\d+\.)\s',s):flush();story.append(para(s));i+=1;continue
  buf.append(s);i+=1
 flush();return story
def build(path,out):
 placements.clear()
 doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=51,leftMargin=51,topMargin=48,bottomMargin=45,title=path.stem,author='知识图谱课程报告')
 doc.build(markdown_flow(path),onFirstPage=footer,onLaterPages=footer)
 if placements:
  reader=PdfReader(out);writer=PdfWriter();writer.clone_document_from_reader(reader);sources={}
  for target,source,index,x,y,w,h in placements:
   if source not in sources:sources[source]=PdfReader(source)
   page=sources[source].pages[index];sw=float(page.mediabox.width);sh=float(page.mediabox.height)
   writer.pages[target].merge_transformed_page(page,Transformation().scale(w/sw,h/sh).translate(x,y),over=True)
  temp=out.with_suffix('.vector.pdf');writer.write(temp);temp.replace(out)
 return len(PdfReader(out).pages)
def run():
 paths=[root/'报告成稿'/'知识图谱课程报告.md']+[root/'翻译源稿'/n for n in ['01_SAC-KG.md','02_KGP.md','03_G-Retriever.md','04_FastToG.md','05_HippoRAG2.md']]
 results=[];outputs=[]
 for p in paths:
  folder=root/('报告成稿' if p.parent.name=='报告成稿' else '中文翻译PDF');folder.mkdir(exist_ok=True)
  out=folder/(p.stem+'.pdf');pages=build(p,out);outputs.append(out);results.append(dict(file=str(out.relative_to(root)),pages=pages,source=str(p.relative_to(root))))
 # 总册前置纸质目录，分册页码保持独立，PDF书签提供电子导航。
 cover=root/'构建与核验'/'总册目录.pdf';listing=[];start=3
 listing.extend([para('知识图谱课程报告与五篇论文中文译稿','h1'),para('面向大语言模型的知识图谱构建、检索与推理技术研究','h2'),para('以 GraphRAG 与长期记忆为例'),Spacer(1,20),para('总册目录','h2')])
 for o,r in zip(outputs,results):
  listing.append(para(f'{o.stem}　总册第 {start} 页起　分册 {r["pages"]} 页'))
  start+=r['pages']+(r['pages']%2)
 listing.extend([Spacer(1,24),para('阅读说明','h2'),para('正文为综合分析与研究设想；五篇译稿保持原文顺序，参考文献保留英文。图表中的机器字段、实体标识及原图英文标签保留，配中文图注与说明。所有实验数字来自原论文；研究设想尚未实验验证。'),para('总册页序用于装订定位，各分册页脚单独编号。分册之间为双面打印加入空白页。可编辑源稿、原始PDF、逐页核验及构建脚本随交付包提供。'),para('版本：2026年11月17日　二轮审校版。已完成逐页内容对照，图内文字未全部中文重绘，审校边界见交付说明。')])
 SimpleDocTemplate(str(cover),pagesize=A4,leftMargin=51,rightMargin=51,topMargin=55,bottomMargin=45).build(listing,onFirstPage=footer,onLaterPages=footer)
 writer=PdfWriter();writer.append(cover,outline_item='总册目录')
 if len(writer.pages)%2:writer.add_blank_page(width=W,height=H)
 for o in outputs:
  writer.append(o,outline_item=o.stem)
  # 每个独立分册从双面打印的正面开始。
  if len(writer.pages)%2:writer.add_blank_page(width=W,height=H)
 total=root/'报告成稿'/'知识图谱课程报告_含五篇译稿.pdf'
 writer.write(total)
 results.append(dict(file=str(total.relative_to(root)),pages=len(writer.pages)))
 (root/'构建与核验'/'pdf_manifest.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(results,ensure_ascii=False,indent=2))
if __name__=='__main__':run()
