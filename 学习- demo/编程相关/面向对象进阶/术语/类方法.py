'''
类方法
    类属性就是针对类对象定义的属性
        使用赋值语句在class关键字下方可以定义类属性
        类属性用于记录与这个类相关的特征
    类方法就是针对类对象定义的方法
        在类方法内部可以直接访问类属性或者调用其他的方法
        语句如下
            @classmethod
            def 类方法名(cls):
                pass

        类方法需要调用修饰器@classmethod 来标识, 告诉解释器这是一个类方法
        类方法第一个参数应该是cls
            由哪一个类调用的方法,方法内部的cls就是哪一个类的引用
            这个参数和实例方法的第一个参数是self类似
            提示使用其他名称也可以,不过习惯用cls
        通过类名.调用类方法,调用方法时,不需要传递cls参数
        在方法内部
            可以通过cls.访问类的属性
            也可以通过cls.调用其他的方法
'''

class Tool:
    count = 0
    # 创建一个类方法
    @classmethod
    def show_tool_count(cls):
        print(f'类方法: 工具对象的数量: {cls.count}')

    # 实例方法
    def show_tool_count_2(self):
        print(f'实例方法: 工具对象的数量: {self.count}')

    # 声明一个初始化函数
    def __init__(self, name):
        self.name = name

        Tool.count += 1

# 创建工具对象
tool1 = Tool('斧头')
tool2 = Tool('榔头')

# 调用类方法
Tool.show_tool_count()


# 通过对象调用实例属性
tool1.show_tool_count_2()

# 实例方法时不可以通过类调用的
# Tool.show_tool_count_2(self.count)