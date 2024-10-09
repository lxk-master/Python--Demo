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

    # 重写父类方法
    def bark(self):
        print('叫的跟神一样')


# 创建对象
xtq = xiaotianquan()
xtq.bark()

'''
啸天犬与普通的狗叫声不一样
    需要修改当前的bark方法
    但是关于狗的方法不能修改
    
想要完成上述功能
    需要进行重写
    
在子类中重写了父类的方法后
    在进行调用时会执行子类中重写的方法
'''