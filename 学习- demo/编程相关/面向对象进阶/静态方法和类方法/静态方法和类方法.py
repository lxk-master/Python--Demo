class Triangle(object):
    """三角形类"""

    def __init__(self,a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    # 装饰器
    # @staticmethod
    # def is_valid(a, b, c):
    #     """判断三角边长能否构成三角形(静态方法)"""
    #     return a + b > c and b + c > a and a + c > b

    # 装饰器
    @classmethod
    def is_valid(cls, a, b, c):
        """判断三条边长能否构成三角形(类方法)"""
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p- self.c)) ** 0.5

# 通过调用类计算三角形的周长
triangle = Triangle(3, 4, 5)
print(triangle.perimeter())

print(Triangle.is_valid(3, 4, 5))
'''
在调用静态方法时不需要对当前类进行实例化
    可以直接使用类名.方法
'''

'''
静态方法与类方法的区别
    静态方法传入的参数都是普通参数
    
    类方法的参数第一位必须是cls
        class
        代表当前的方法时属于当前的类
        
    静态方法是不和当前类进行绑定的
        可以看成一个单独的函数
'''