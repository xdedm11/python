from pandas import Series
from pandas import DataFrame

aSer=Series([1,2.0,'a'])
#print(aSer)
#print(aSer.index,aSer.values)

data={'name':['wdc','ll','ny'],'pay':[4,5,6]}
frame=DataFrame(data)
print(frame)
'''
frame['name']='nick'
del frame['pay']
print(frame)
'''
print(frame.pay.min())
print(frame[frame.pay>=5])