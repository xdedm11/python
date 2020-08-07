import requests
import urllib
from bs4 import BeautifulSoup
import re
import os

url='https://cn.bing.com/images/search?q=%E4%BA%92%E8%81%94%E7%BD%91%E4%BC%81%E4%B8%9Alogo&qs=n&form=QBIR&sp=-1&pq=%E4%BA%92%E8%81%94%E7%BD%91%E4%BC%81%E4%B8%9Alogo&sc=0-9&sk=&cvid=C323EE36B1844BDC9BD7E6581AAF83C3'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
string = soup.select('img')
print(string)
root=r'C:\Users\薛定谔的猫\图片'
pattern = r'^https://(.|\n)*pid=1.1$'
web = re.findall(pattern,string)
print(web)
getimg(web)


def getimg(web):
    for url in web:
        path = root + web.split('/')[1]
        try:
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print('save successfully')
        except:
            print('false')
