# class A:
#     def work(self):
#         print('人类需要工作')
#
# class B(A):
#     def work(self):
#         print('程序员在工作 -- 代码')
#
# class C(A):
#     def work(self):
#         print('设计师在工作 -- 图纸')
#
# b = B()
# c = C()
#
# b.work()
# c.work()

class Dog:
    # 定义类属性
    def __init__(self, name):
        self.name = name

    # 方法
    def game(self):
        print('%s 在蹦蹦跳跳的玩耍...' % self.name)


class XiaoTianDog(Dog):
    # 当前的哮天犬和普通的狗不一样
    '''
    子类继承父类的时候,具有父类所有的属性和方法
    '''
    def game(self):
        print('%s 飞到天上去玩耍...' % self.name)

class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        # 让狗玩耍
        dog.game()
        # 让狗与人一起玩耍
        print('%s 和 %s 快乐的玩耍' % (self.name, dog.name))

# 创建一个普通狗对象
wangcai = Dog('旺财')

wangcai = XiaoTianDog('飞天旺财')
# 创建一个人的对象
xiaoming = Person('小明')

# 调用人类中的game_with_dog方法
xiaoming.game_with_dog(wangcai)


'''
多态的运行情况
    我们在调用子类中的同名方法时 输出的值不一样
    
    基于继承和重写的
'''