import requests
import os
url='https://youtu.be/-lEcOmu3x3s'
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