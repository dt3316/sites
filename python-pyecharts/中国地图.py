
from pyecharts import Map

value = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
attr = ['武汉市','襄阳市','荆州市','荆门市','宜昌市','仙桃市','十堰市','天门市','潜江市','黄冈市','黄石市','咸宁市','孝感市','随州市','鄂州市','神农架林区','恩施土家族苗族自治州']
map = Map("湖北省", width=1200, height=600)
map.add("", attr, value, maptype='湖北', is_visualmap=True, visual_text_color='#000')

map.show_config()
map.render('湖北省.html')
