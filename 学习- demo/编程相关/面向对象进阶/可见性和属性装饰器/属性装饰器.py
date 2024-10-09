'''
Python中可以通过property装饰器为“私有”属性提供读取和修改的方法
装饰器通常会放在类、函数或方法的声明之前,可以通过@符号来表示将装饰器应用于类、函数或方法
'''

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    # 属性访问器(getter方法) - 获取__name属性
    @property
    def name(self):
        return self.__name

    # 属性修改器(setter方法) - 修改__name属性
    @name.setter
    def name(self, name):
        self.__name = name or '无名氏'

    # 获取私有属性
    @property
    def age(self):
        return self.__age

stu = Student('顾安', 20)
print(stu.age, stu.name)
stu.name =  ''
print(stu.name)


# stu.age = 30
# print(stu.age)   # AttributeError: property 'age' of 'Student' object has no setter  没有设置setter