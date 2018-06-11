#coding=utf-8
import re
import requests

url = 'http://eyval.net/10224'

#设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

#用get方法打开url并发送headers
html = requests.get(url, headers = header)

phone = html.text
it = re.finditer(r'(R960x0.*? )', phone)
for match in it:
    print(match.group())
    pichtml = requests.get('http://img1.daumcdn.net/thumb/' + match.group())
    filename = match.group()[1:5] + '_' + match.group()[67:77] + '.jpg'
    #图片不是文本文件，以二进制格式写入，所以是html.content
    f = open('C:\\Users\\william\\Pictures\\mano erina\\' + filename, 'wb')
    f.write(pichtml.content)
    f.close()
