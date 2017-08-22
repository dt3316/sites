from pyecharts import EffectScatter


wh = [1,2,3,4,5,6,7,8,9,10]
yc = [11,21,31,41,51,61,71,81,91,111]
v2 = [0,10,20,30,40,50,60,70,80,90]
es = EffectScatter("动态散点图示例")
es.add("武汉", wh, v2,symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
es.add("宜昌", yc, v2,symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")



es.render('湖北16地市.html')