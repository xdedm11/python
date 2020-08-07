import requests
import time

def getHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return 'false'

if __name__ == '__main__':
    url='http://www.baidu.com'
    start = time.perf_counter()
#   print(getHtmlText(url))
    for i in range(101):
        getHtmlText(url)
    t=time.perf_counter()-start
    print(t)

