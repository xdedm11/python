money=input()
if money[0:3]=='RMB':
    usd=eval(money[3:])/6.78
    print('USD{:.2f}'.format(usd))
elif money[0:3]=='USD':
    rmb=eval(money[3:])*6.78
    print('RMB{:.2f}'.format(rmb))
else:
    print('wrong')
