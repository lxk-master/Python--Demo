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


class xiaotianquan(Dog):
    def fly(self):
        print('我会飞')

    def bark(self):
        # 在当前方法中调用父类方法
        # 使用super方法
        print('叫的跟神一样')
        # super() 也是一个对象
        # super().bark()

        # 另外一种调用方式 在Python3中被保留
        # 一定要加上self,不可以被省略
        # Dog.bark(self)

        # 在当前方法中通过子类.方法的方式调用方法
        # 递归循环 在当前的方法体中调用自身 会出现递归的情况。结果就是死循环
        xiaotianquan.bark(self)

        # 当前的子类方法进行扩展
        print('这是一个测试...')

# 创建xtq对象
xtq = xiaotianquan()
xtq.bark()