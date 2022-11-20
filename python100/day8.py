from math import sqrt
from time import time, localtime, sleep
from abc import ABCMeta, abstractmethod

class Person(object):

    """slots可以限制类的属性添加，否则类可以添加各种属性"""
    __slots__  = ('_name', "_age", "_gender")

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age
    
    # 修改器 - getter方法
    @age.setter
    def age(self, age):
        self._age = age
    
    def paly(self):
        print("%s正在愉快的玩耍" % self._name)

    def is_watch(self):
        if self._age >= 18:
            print("%s正在观看爱情动作片" % self._name)
        else:
            print("%s只能看熊出没" % self._name)


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a,b,c):
        return a + b > c and b + c >a and a + c > b
    
    def perimeter(self):
        return self._a + self._b +self._c
    
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half*(half-self._a) * (half - self._b) * (half - self._c))



class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute =0, second=0):
        self._hour = hour
        self._minute  = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour +=1
                if self._hour == 24:
                    self._hour = 0
    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
            (self._hour, self._minute, self._second)

class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self._grade = grade
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self,grade):
        self._grade = grade
    
    def study(self,course):
        print("%s的%s正在学习%s." % (self._grade, self._name, course) )
    

class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property 
    def title(self, title):
        self._title = title
    
    @title.setter
    def title(self, title):
        self._title = title
    
    def teach(self, course):
        print("%s%s正在教%s" % (self._name, self._title, course))

class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname
    
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass

class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s:汪汪汪...' % self._nickname)

class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s:喵...喵...' % self._nickname)



def main():
    # person = Person('东风谷早苗', 16)
    # person.play()
    # person.age = 18
    # person.play()
    # # person.city = 'beijing'
    # # print("居住的城市是%s" % person.city) #居住的城市是beijing
    # person._gender = '男'
    # print("%s"%person._gender)

   
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a,b,c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接受消息的对象作为参数
        # print(Triangle.periment(t))
        print(t.area())
        # print(triangle.area(t))
    else:
        print("无法构成三角形，")


    # 通过类方法创建对象并获取系统时间
    # clock = Clock.now()

    # while True:
    #     print(clock.show())
    #     sleep(1)
    #     clock.run()
        
    stu = Student('博丽灵梦', 16 , '初三')
    stu.study("数学")
    Student.is_watch(stu)

    te = Teacher("八云紫",38,"砖家")
    te.teach("八卦封印阵")
    te.is_watch()


    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()


