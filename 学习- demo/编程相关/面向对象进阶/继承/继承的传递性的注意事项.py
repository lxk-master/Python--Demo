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

class Dog(Animal):
    def bark(self):
        print('汪汪叫')

class XiaoTianQuan(Dog):
    def fly(self):
        print('我会飞')

class Cat(Animal):
    def catch(self):
        print('抓老鼠')

# 创建对象
xtq = XiaoTianQuan()
xtq.fly()
xtq.bark()
xtq.eat()

# 定义了一个猫类,继承自动物类
# 自身实现了一个方法: 抓老鼠
# 现在通过xtq对象是否可以调用猫类的方法

# 当前的啸天犬对象并没有和猫类进行绑定(继承)
# 一定要分清当前类的继承关系
# xtq.catch()