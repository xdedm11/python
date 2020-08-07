try:
    f=open('NEWS.txt')
    for line in f:
        print(line,end="")
except IOError:
    print('fail')
finally:
    f.close()
