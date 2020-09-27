# python成员函数、变量均默认public，定义私有成员在其前加__,私有成员在类外部也可以调用
print('''
_xxx:保护成员，不能用from module import *导入，只有类对象和子类对象可访问
__xxx:私有成员，一般只有类对象自己能访问，也可以对象名._类名__xxx来访问
__xxx__:系统定义的特殊成员
''')
#import sys
#sys.setrecursionlimit(10000)

class Student:
    ''' Student为学生类'''
    # self 代表类的实例
    def __init__(self,name,age):
        super(Student,self).__init__();
        self._name=name
        self.__age=age
    def get_name(self):
        print(self._name)
    def __get_age(self):
        print(self.__age)
    def info(self,name):
        print("My name is",name,'.')

print(Student.__doc__)

if __name__=='__main__':
    # __name__是当前模块名，模块直接运行时为__main__
    student=Student('Delicate',21)
    print(dir(student))
    print(student._name)
    student.get_name()
    print(student._Student__age)
    student._Student__get_age()



class Car(object):
    # python3.x的所有类都是object的子类
    # 属于类的数据成员：该类所有对象共享，不在任何成员方法中定义，可以通过类名或对象名访问
    price=10
    def __init__(self,color):
        # 属于对象的数据成员：定义/使用时必须以self作为前缀
        self.color=color

if __name__=='__main__':
    car1=Car('red')
    car2=Car('blue')
    print(car1.color,car2.color)
    # 修改类的属性
    Car.price=11
    # 动态增加类的属性
    Car.name='motor'
    print(car1.color,Car.price,Car.name)

    def set_speed(self,speed):
        self.speed=speed

    import types
    # 动态为对象增加成员方法
    car1.set_speed=types.MethodType(set_speed,car1)
    car1.set_speed(50)
    print(car1.speed)

'''
实例方法：方法中访问需要以self为前缀，外部通过对象名时不用      
    公有方法：通过对象名直接调用
    私有方法：以__开始，通过self调用，外部 对象名._类名__xxx 
类方法:cls作为第一个参数表示类本身 @classmethod装饰器 可直接用类名调用，也可以通过实例访问  类方法内可通过cls访问类的数据、类方法和静态方法
静态方法:@staticmethod装饰器 可直接用类名调用，也可以通过实例访问  类方法内可访问类的数据、类方法和静态方法
'''
class Test(object):
    '''docstring for test'''
    hello_world='hello world!'
    def __init__(self,arg=None):
        super(Test,self).__init__()
        self.arg=arg
    def say_hello(self):
        print('公有方法say_hello():','hello world')
        #类内调用私有方法
        self.__say_hello()
    def __say_hello(self):
        print('私有方法__say_hello():','hello world')
    @staticmethod
    def say_bad():
        print('say bad')
        Test.say_nothing()
        Test.say_good()
        print(Test.hello_world)
    @staticmethod
    def say_nothing():
        print('say nothing')
    @classmethod
    def say_good(cls):
        print('say good')
        print(cls.hello_world)  #通过cls访问类的数据
        #cls.say_bad()
        print('!!!小心调用函数形成递归!!!')
        #cls.say_hello()        类方法内不能访问实例方法

def main():

    test=Test() #实例化
    test.say_hello() #类内调用私有方法
    test._Test__say_hello() #外部 对象名._类名__xxx

    Test.say_bad()
    Test.say_good()
    print('\n')

    test.say_bad()
    test.say_good()

if __name__ == '__main__':
    main()

'''
属性
    类属性：
    实例数据属性
'''
'''
class Animal(object):
    count=0  # 类属性
    def __init__(self,name,age):
        Animal.count=Animal.count+1
        # 实例属性
        self.name=name
        self.age=age
if __name__ == '__main__':
    dog=Animal('Dogger',3)
    print('动物数量：',Animal.count)
    print("Name:",dog.name)
    print("Age",dog.age)
    dog.color='Black'
    print("Color:",dog.color)

    cat=Animal('Kitty',1)
    print('动物数量：', Animal.count)

    def animal_type(self,type):
        self.type=type
        #!!! self.type=self.type
    # 动态为类增加成员方法
    Animal.animal_type=types.MethodType(animal_type,Animal)

    blackCat=Animal('black cat',2)
    blackCat.animal_type("波斯猫")
    #!!! blackCat.animal_type="波斯猫"
    print('动物数量：', Animal.count)
    print("动物类型:", blackCat.animal_type)
'''
class Animal(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age
        self._color='Black'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value,str):
            self._name=value
        else:
            self._name='No name'

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        if value>0 and value<100:
            self._age=value
        else:
            self._age=0

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,value):
        self._color=value
if __name__ == '__main__':
    dog=Animal('Dogger',3)
    print("Name:",dog.name)
    print("Age",dog.age)

    dog.name='Kitty'
    dog.age=1
    print("Name:", dog.name)
    print("Age", dog.age)

print("\n继承 super")
class Person(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        print("Person类__init__()。","姓名：",self.name)

class Student(Person):
    def __init__(self,name,gender,score):
        super(Student, self).__init__(name, gender)
        # super().__init__(name,gender)
        self.score=score
        print("Student类__init__()。","姓名：",self.name)
if __name__ == '__main__':
    person=Person("PersonName","男")
    student=Student("StudentName","男",100)

print("\n多重继承")
class P1():
    def foo(self):
        print("p1-foo")

class P2():
    def foo(self):
        print("p2-foo")

    def bar(self):
        print("p2-bar")

class C1(P1,P2):
    pass

class C2(P1,P2):
    def bar(self):
        print("C2-bar")

class D(C1,C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d=D()
    d.foo()
    d.bar()

print("\n多态")
class Dog(object):
    def work(self):
        pass

class ArmyDog(Dog):
    def work(self):
        print("追击敌人")

class DrugDog(Dog):
    def work(self):
        print("追查毒品")

class Person(object):
    def work_with_dog(self,dog):
        dog.work()

person=Person()
person.work_with_dog(ArmyDog())
person.work_with_dog(DrugDog())

print("\n del删除对象时自动调用析构函数__del__()")