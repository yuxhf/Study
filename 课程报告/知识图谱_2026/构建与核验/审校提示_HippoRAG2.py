from pathlib import Path
b=Path('E:/GroupMT/study-report/课程报告/知识图谱_2026');p=b/'翻译源稿/05_HippoRAG2.md';s=p.read_text(encoding='utf8')
s=s.replace('Fleetboston Financial，被收购方为，Bank of America','Fleetboston Financial，收购方为，Bank of America')
s=s.replace('Bernhard Lichtenberg，被册封为真福者，Catholic Church天主教会','Bernhard Lichtenberg，由其册封为真福，Catholic Church天主教会')
# Translate natural-language object values in the translated JSON, retaining proper-name identifiers.
for a,z in {'1 october 1943':'1943年10月1日','15 february 1950':'1950年2月15日','4 october 1971':'1971年10月4日','october 14 1982':'1982年10月14日','28 december 1981':'1981年12月28日','december 5 1983':'1983年12月5日','10 march 1973':'1973年3月10日','26 november 2018':'2018年11月26日','18 august 1934':'1934年8月18日','1980 american thriller crime drama film':'1980年美国惊悚犯罪剧情片','1960 french comedy film':'1960年法国喜剧片','1968 hindi language drama film':'1968年印地语剧情片','hindi films':'印地语电影','old mother riley series of films':'Old Mother Riley系列电影'}.items():
 s=s.replace('"'+a+'"','"'+z+'"')
s=s.replace('"处于该区域的","east"','"位于…侧","东"').replace('"是","islet"','"是","小岛"')
s=s.replace('非自然语言实体类型可按词义读取','原例中的类型和方位等自然语言值也已在JSON译为中文，其英文对应为')
p.write_text(s,encoding='utf8')
print('fixed relation direction and prompt natural-language values')
