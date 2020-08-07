#calpy2.py
from random import random
from time import perf_counter
num=1000*1000
cyclein=0
start=perf_counter()
for i in range(1,num+1):
    x,y=random(),random()
    dis=pow(x**2+y**2,0.5)
    if dis<=1:
        cyclein+=1
pi=4*(cyclein/num)
print('pi is:{}'.format(pi))
print('time is:{}'.format(perf_counter()-start))
