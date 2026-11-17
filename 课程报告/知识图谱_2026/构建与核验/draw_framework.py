from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).resolve().parents[1];out=root/'报告成稿'/'assets';out.mkdir(exist_ok=True)
font='C:/Windows/Fonts/simhei.ttf'
def make(name,title,boxes,sub):
 im=Image.new('RGB',(1600,580),'white');d=ImageDraw.Draw(im)
 f=ImageFont.truetype(font,32);sm=ImageFont.truetype(font,25);hd=ImageFont.truetype(font,40)
 d.text((65,35),title,font=hd,fill='#17232e')
 for i,(a,b) in enumerate(boxes):
  x=65+i*306;y=155
  d.rounded_rectangle((x,y,x+270,y+205),radius=9,fill='#f1f4f5',outline='#40586a',width=2)
  d.text((x+18,y+28),a,font=f,fill='#17232e')
  for j,line in enumerate(b.split('\n')):d.text((x+18,y+88+j*38),line,font=sm,fill='#394a55')
  if i<len(boxes)-1:
   xx=x+281;d.line((xx,y+100,xx+19,y+100),fill='#40586a',width=4);d.polygon([(xx+19,y+100),(xx+8,y+93),(xx+8,y+107)],fill='#40586a')
 for j,line in enumerate(sub.split('\n')):d.text((65,410+j*44),line,font=sm,fill='#394a55')
 im.save(out/name)
make('method_map.png','图1 五篇论文在证据获取中的位置',[
 ('可信构图','SAC-KG\n生成 验证 剪枝'),('文段导航','KGP\n逐步找下一跳'),('结构选择','G-Retriever\n相关连通子图'),('社区探索','FastToG\n宽度 深度 成本'),('关联复用','HippoRAG 2\n三元组 文段 PPR')],
 '本图为报告作者依据五篇方法绘制的概念组织图。\n箭头表示本文的讲解顺序，不表示论文继承关系，也不表示五个系统已被串联实现。')
make('research_framework.png','图2 可追溯多粒度检索的研究设想',[
 ('来源入库','文段与三元组\n保留版本与定位'),('联合召回','词汇 向量 图\n维护多个入口'),('粒度选择','文段 路径\n子图 社区'),('来源核验','答案事实对齐\n冲突与缺口检测'),('局部补检','预算内补证据\n不足则保留不确定')],
 '研究状态：框架提案，尚未实现或验证；各模块的贡献需要统一预算下的消融实验。\n更新与撤销贯穿全流程，缓存须绑定语料版本；相似性边只能导航，不能直接充当事实。')
print(out)
