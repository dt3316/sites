from pyecharts import WordCloud

name = ['武汉市','襄阳市','荆州市','荆门市','宜昌市','仙桃市','十堰市','天门市','潜江市','黄冈市','黄石市','咸宁市','孝感市','随州市','鄂州市','神农架林区','恩施土家族苗族自治州']

value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555,
         550, 462, 366, 360]
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.show_config()
wordcloud.render('词云.html')
