import requests
import os
url='https://tse4-mm.cn.bing.net/th?id=OIP.2bmkW2e6JDRxS1cKkiFdpQHaD3&amp;w=230&amp;h=170&amp;rs=1&amp;pcl=dddddd&amp;o=5&amp;pid=1.1'
root=r'C:\Users\薛定谔的猫\图片'
path=root+url.split('/')[-1]
try:
    r = requests.get(url)
    with open(path,'wb') as f:
        f.write(r.content)
        f.close()
        print('save successfully')
except:
    print('false')