print("列表 list")
list_range=list(range(5))
print(list_range)
print(list_range[0],list_range[-1],list_range[1:3])
list_range[0]='t'
print(list_range[0:3])
del list_range[4]
print(list_range)
list_range.append(' ')
print(list_range)

print("\n元组 tuple")
#无法更改，只有一个元素也要在元素后加，
tuple_number=(1,2,3,4)
print(tuple_number)
tuple_list=tuple(list_range)
print(tuple_list)
print(tuple_list[0],tuple_list[-2])

print("\n字典 dict")
#键不可变
dict_db_server={"server":"localhost","database":"mysql","user":"root"}
keys=['t','b','g']
values=['turtle',' ','graphics']
dict_info=dict(zip(keys,values))
print(dict_db_server)
print(dict_info)
dict_db_server['server']='dbserver'
print(dict_db_server['server'])
if('password' in dict_db_server):
    print(dict_db_server['password'])
else:
    print('password不存在')
print("get访问'password'的值:",dict_db_server.get('password','"password"不存在'))
print("默认遍历键")
for item in dict_db_server:
    print(item)
print("items()遍历'键：值':")
for item in dict_db_server.items():
    print(item)
print("items()遍历'键：值':;key与value获取具体值")
for key,value in dict_db_server.items():
    print("键：",key,"值：",value)
print("keys()遍历键:")
for key in dict_db_server.keys():
    print(key)
print("values()遍历值:")
for value in dict_db_server.values():
    print(value)
print(dict_info.keys())
print(dict_info.values())

print("\n集合 set")
#集合元素不可变
set_range=set(range(1,5))
print(set_range)
set_range.add(666)
print(set_range.pop()) #随机删除
print(set_range)

print("\n字符串")
str1='hello world'
str2="python"
print(str1[0])
print(str2[2:6])
print(str1[:6]+str2[:6])
name="Delicate"
age=21
print('%s今年%d岁'%(name,age))
print('{yourname}今年{yourage}岁'.format(yourname=name,yourage=age))
print(f'{name}今年{age}岁')