class Student:

    def __init__(self,name, age):
        # 创建私有属性
        self.__name = name
        self.__age = age

    def study(self,course_name):
        print(f'{self.__name}正在学习{course_name}.')

stu = Student('王大锤', 20)
stu.study('Python程序设计')
# print(stu.__name)
'''
上述最后一行代码会引发 AttributeError: 'Student' object has no attribute '__name' 错误
由此可见,以__开头的属性__name是私有的,在类的外面无法应用,但是类的里面study方法中可以通过self.__name访问该属性
'''

'''
提醒:
    Python并没有从语法上严格保证私有属性的私密性,他只是给私有的属性和方法换了一个名字来阻挠对它们的访问.
    事实上,如果你知道更换名字的规则仍然可以访问到它们
'''
print(stu._Student__name, stu._Student__age)
'''
Python中有一句名言: We are all consenting adults here (大家都是成年人)
Python语言的设计者认为程序员要为自己的行为负责,而不是由Python本身来严格限制访问的可见性
而大多数的程序员都认为开放比封闭要好,把对象的属性私有化并不是编程语言必须的东西,所以Python并没有从语法上做出严格的限制
'''
