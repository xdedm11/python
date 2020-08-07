import jieba
import wordcloud
from scipy.misc import imread
mask=imread('environment.jpg')
f=open('threekingdoms.txt',encoding='utf-8')
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=' '.join(ls)
w=wordcloud.WordCloud(mask=mask,font_path='msyh.ttc',width=1000,height=800,background_color='white',max_words=16)
w.generate(txt)
w.to_file('threekingdoms.jpg')
