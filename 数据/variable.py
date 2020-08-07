def f(x):
    global a
    print(a)
    a=4
    print(a)

a=3
f(9)
print(a)
