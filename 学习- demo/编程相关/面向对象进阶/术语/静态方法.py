'''
在开发时,如果需要在类中封装一个方法,这个方法:
    既不需要访问实例属性或者调用实例方法
    也不需要访问类属性或者调用类方法
这个时候,就可以把这个方法封装成一个静态方法
语法如下:
    @staticmethod
    def 静态方法名():
        pass

静态方法需要使用修饰器@staticmethod 来标识,告诉解释器这是个静态方法
通过类名.调用静态方法
'''

class Dog(object):
    # 狗对象计数
    dog_count = 0
    # 创建静态方法
    @staticmethod
    def run():
        # 不需要访问实例属性也不需要访问类属性的方法
        print('狗在跑...')

    def __init__(self, name):
        self.name = name

# 静态方法不需要创建对象就可以使用
Dog.run()