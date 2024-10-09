'''
开发两个类
    动物类
        四个特性:
            吃
            喝
            跑
            睡
    狗类
        特性
            吃
            喝
            跑
            睡
            汪汪叫
'''

# 定义一个动物类
class Animal:
    def eat(self):
        print('吃')

    def drink(self):
        print('喝')

    def run(self):
        print('跑')

    def sleep(self):
        print('睡')

# 定义一个狗类
class Dog:
    def eat(self):
        print('吃')

    def drink(self):
        print('喝')

    def run(self):
        print('跑')

    def sleep(self):
        print('睡')

    def bark(self):
        print('汪汪叫')


# 创建一个对象
wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()

# 想让旺财汪汪叫
wangcai.bark()

'''
当前动物类和狗类的四个方法已经重复了
    代码有冗余
    解决这样的代码重用的方法
'''