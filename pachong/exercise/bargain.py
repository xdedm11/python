import requests
import re

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def parsePage(ilt,html):
    try:
        plt = re.findall(r'￥</em><i>[\d\.]*', html)
        tlt = re.findall(r'a target="_blank" title=".*?"', html)
        for i in range(len(plt)):
            price=eval(plt[i].split('<i>')[1])
            title=eval(tlt[i].split('title=')[1])
            ilt.append([price,title])
    except:
        print('')

def printGoodsList(ilt):
    tplt='{:4}\t{:8}\t{:16}'
    print(tplt.format('序号','价格','商品名称'))
    count=0
    for g in ilt:
        count += 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods='书包'
    url='https://search.jd.com/Search?keyword='+goods+'&enc=utf-8&wq='+goods
    print(url)
    infoList=[]
    try:
        html = getHTMLText(url)
#        print(html)
        parsePage(infoList, html)
    except:
        print('get false')
    printGoodsList(infoList)

main()