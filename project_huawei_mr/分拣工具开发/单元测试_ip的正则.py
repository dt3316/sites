

=============测试通过的片段IP地址，准备封装。

ip_text = "10.26.192.13-黄石BSC10"
def derive_ip(ip_text):
	#text 为传入的参数
	  
	#ip地址的的正则表达式 
	ip_re = re.compile('((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))') 
	result = ip_re.finditer(ip_text) 
	for m in result: 
	  myip = m.group()
	  return myip #同文件名返回IP
derive_ip(ip_text)

d = {'黄石BSC10': '10.26.192.23', '黄石BSC11': '10.26.192.24', '黄石BSC12': '10.26.192.25', '黄石BSC13': '10.26.192.27', '黄石BSC14': '10.26.192.29', '黄石BSC15': '10.26.192.31', '黄石BSC16': '10.26.192.33', '黄石BSC17': '10.26.192.35', '黄石BSC02': '10.26.192.236', '黄石BSC04': '10.26.192.237', '黄石BSC05': '10.26.192.238', '黄石BSC07': '10.26.192.20', '黄石BSC08': '10.26.192.21', '黄石BSC09': '10.26.192.22'}

BSC = '黄石BSC10'

def bsc2ip():
	pass
	return d[BSC]
bsc2ip() #返回ip

ip_bsc_dict ={'10.26.192.23': '黄石BSC10', '10.26.192.24': '黄石BSC11', '10.26.192.25': '黄石BSC12', '10.26.192.27': '黄石BSC13', '10.26.192.29': '黄石BSC14', '10.26.192.31': '黄石BSC15', '10.26.192.33': '黄石BSC16', '10.26.192.35': '黄石BSC17', '10.26.192.236': '黄石BSC02', '10.26.192.237': '黄石BSC04', '10.26.192.238': '黄石BSC05', '10.26.192.20': '黄石BSC07', '10.26.192.21': '黄石BSC08'}

{value:key for key,value in ip_bsc_dict.iteritems()}


d = {'黄石BSC10': '10.26.192.23', '黄石BSC11': '10.26.192.24', '黄石BSC12': '10.26.192.25', '黄石BSC13': '10.26.192.27', '黄石BSC14': '10.26.192.29', '黄石BSC15': '10.26.192.31', '黄石BSC16': '10.26.192.33', '黄石BSC17': '10.26.192.35', '黄石BSC02': '10.26.192.236', '黄石BSC04': '10.26.192.237', '黄石BSC05': '10.26.192.238', '黄石BSC07': '10.26.192.20', '黄石BSC08': '10.26.192.21', '黄石BSC09': '10.26.192.22'}

l1=['test','k2']
l2=[5,7]
d=dict(zip(l1,l2))
d
{'test': 5, 'k2': 7}







