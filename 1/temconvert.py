#temconvert.py
tem=input()
if tem[0]=='F':
    c=(eval(tem[1:])-32)/1.8
    print('转换后温度C{:.2f}'.format(c))
elif tem[0]=='C':
    f=1.8*eval(tem[1:])+32
    print('转换后温度F{:.2f}'.format(f))
else:
    print('it is wrong')
