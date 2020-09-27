def draw_mathmatics(n,len=150):
    '''
    功能：绘制正n边形
    '''
    print('''
    a
    b
    c #ddd
    ''')
    import turtle
    angle=360/n
    turtle.shape('turtle')
    turtle.pensize(5)
    turtle.color('red','green')
    for _ in range(n):
        turtle.forward(len)
        turtle.right(angle)
    return

print('\n默认参数 可变对象')
def add_to_list(list=None):
    if list is None:
        list=[]
    list.append('end')
    return list
print(add_to_list([1,2,3]))
print(add_to_list())    #重复调用不会叠加

print('\n可变参数 前加* 允许传入[1,无穷)')
def sum(*numbers):
    num_sum=0
    for num in numbers:
        num_sum+=num
    return num_sum
print(sum(1,2,3))

print('\n关键字参数 前加** 允许传入[0,无穷) 可作为可选项')
def sum2(**numbers):
    num_sum=0
    for key,value in numbers.items():
        num_sum+=value
    return num_sum
dict1={'x':1}
print(sum2(**dict1))
print("顺序是：必选参数、默认参数、可变参数与关键字参数")

print("\n返回多个值时相当于返回一个tuple")
def swap(num1,num2):
    return num2,num1
a=1;b=2
print(swap(a,b))
a,b=swap(a,b)
print(a,b)

print("\n作用域 L E G B  模块、类、函数产生新的作用域;修改嵌套作用域中的变量nonlocal")
num=1;
def func_outer():
    num=2
    print("外部函数：",num)
    def func_innner():
        nonlocal num
        num=3
        print("内部函数：",num)
    func_innner()
func_outer()
print("调用后：",num)

print("\nlambda表达式")
print(lambda a,b:a+b)
sum_lambda=lambda a,b:a+b
print(sum_lambda(1,2))

print("\nimport引入模块时，会将引入的模块文件中的代码执行一次（仅在第一次引用时）")
from math import log
print(log(3,3))
import random as rd
print(rd.random())
print(rd.randrange(3,20,2))
import time as tm
tm.clock()
tm1=tm.time()
draw_mathmatics(5,100)
print(tm.clock())
tm2=tm.time()
print(tm2-tm1)