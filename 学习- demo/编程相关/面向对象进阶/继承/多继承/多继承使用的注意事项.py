class A:
    def test(self):
        print('A --- test 方法')

    def demo(self):
        print('A --- demo 方法')


class B:
    def test(self):
        print('B --- test 方法')

    def demo(self):
        print('B --- demo 方法')

class C(B, A):
    pass

# 创建C类对象
c = C()
c.test()
c.demo()

'''
调用顺序与继承顺序有关系
'''

print(C.__mro__)

'''
C
    查询本类中有没有调用的方法
        类B
            类A
                object
                    报错
    从左至右的查询顺序
'''