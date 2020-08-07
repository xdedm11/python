def getNum():
    nums=[]
    inumstr=input('in:')
    while inumstr!='':
        nums.append(eval(inumstr))
        inumstr=input('in:')
    return nums

def mean(numbers):
    s=0
    for num in numbers:
        s=s+num
    return s/len(numbers)

def dev(numbers,mean):
    sdev=0
    for num in numbers:
        sdev+=(num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

List=getNum()
print(List)
Mean=mean(List)
print(Mean)
Dev=dev(List,Mean)
print(Dev)
