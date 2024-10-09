class A:
    def __init__(self):
        self.num_1 = 100
        self.__num_2 = 200

    def __test(self):
        print(f'公有属性与私有属性的值: {self.num_1}, {self.__num_2}')


    # 公有方法
    def test(self):
        print(f'父类中的公有方法输出私有属性: {self.__num_2}')
        # 在公有方法中调用私有方法
        self.__test()



class B(A):
    # 公有方法
    def demo(self):
        # 1. 在子类方法中访问父类的公有属性
        print(f'子类方法输出父类中的公有属性: {self.num_1}')
        # 2. 在子类中调用父类的公有方法输出私有属性
        self.test()


# 对象
b = B()
b.demo()



'''
子类可以通过父类中的公有方法间接访问到私有属性和私有方法
'''