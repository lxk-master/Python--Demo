'''
在Python中可以动态为对象添加属性,这是Python作为动态语言的一种特权,对象的方法其实本质上也是对象的属性,如果给对象发送一个无法接收的消息,引发的异常仍然是AttributeError
'''
class Student:

    # 元组  只允许类里有 name 和 age
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student('王大锤', 30)
# 不修改当前类代码 为Student对象动态添加sex属性
stu.sex = '男'
print(stu.name, stu.age, stu.sex)


'''
如果不希望在使用对象时动态的为对象添加属性,可以使用Python的 __slots__ 魔法
对于Student类来说,可以在类中指定 __slots__ = ('name', 'age'),这样Student类的对象只能有name和age属性,如果想动态添加其他属性会引发异常
'''