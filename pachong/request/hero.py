#爬虫 -- 王者荣耀
import urllib.request
import json
import os #对计算机的操作
#json文件
v_herolist_url = urllib.request.urlopen("http://pvp.qq.com/web201605/js/herolist.json")
#请求
v_herolist = v_herolist_url.read().decode('utf-8')
#字符串的截取BOM脚本
# \xef\xbb\xbf -- python 自动加入的编码方式声明
v_hero = v_herolist.encode('utf8')[3:].decode('utf-8')
#转换json格式
#返回一个变量
hero_json = json.loads(v_hero)
#获取长度
hero_num = len(hero_json)
#皮肤网址
#http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/167/167-bigskin-5.jpg
#创建本地文件夹
hero_dir = 'D:\workspace\myhero\\'
if not os.path.exists(hero_dir):
    os.mkdir(hero_dir)
for num in range(hero_num):
   skinsname =  hero_json[num]['skin_name'].split("|")
   for i in range(len(skinsname)):
        skin_name = hero_json[num]['ename']
        #皮肤的数字标记
        #皮肤地址
        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(skin_name)+'/'+str(skin_name)+'-bigskin-'+str(i+1)+'.jpg'
        #要保存的地址
        save_url=hero_dir+str(skin_name)+"_"+str(i+1)+".jpg"
        urllib.request.urlretrieve(skin_url,save_url)