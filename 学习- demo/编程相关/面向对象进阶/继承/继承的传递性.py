# 定义一个动物类
class Animal:
    def eat(self):
        print('吃---')

    def drink(self):
        print('喝---')

    def run(self):
        print('跑---')

    def sleep(self):
        print('睡---')

# 创建一个狗类
class Dog(Animal):
    def bark(self):
        print('汪汪叫')

# 创建一个啸天犬类
class xiaotianquan(Dog):
    def fly(self):
        print('我会飞')


# 创建啸天犬对象
xtq = xiaotianquan()
xtq.fly()
xtq.bark()

# 使用xtq直接调用动物类中封装的方法
xtq.run()

'''
啸天犬类继承自狗类
狗类继承自动物类

啸天犬是狗类的子类
狗类是动物类的子类

啸天犬类是动物类的子子类



'''