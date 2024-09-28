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

# 定义一个狗类
class Dog(Animal):
    # def eat(self):
    #     print('吃')
    #
    # def drink(self):
    #     print('喝')
    #
    # def run(self):
    #     print('跑')
    #
    # def sleep(self):
    #     print('睡')
    #
    def bark(self):
        print('汪汪叫')


# 创建一个对象
wangcai = Dog()
wangcai.bark()
wangcai.sleep()
wangcai.eat()
wangcai.run()
wangcai.drink()