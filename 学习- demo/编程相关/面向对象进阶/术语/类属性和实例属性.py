'''
概念和使用
    类属性就是给类对象中定义的属性
    通常用来记录这个类相关的特征
    类属性不会用于记录具体对象的特征
'''

class Tool(object):
    # 使用赋值语句定义类属性,记录创建工具对象的总数
    count = 0
    def __init__(self,name):
        self.name = name

        #   针对类属性做一个计数 当我们创建对象之后让 count + 1
        Tool.count += 1

# 创建工具对象
tool1 = Tool('斧头')
print(Tool.count)
tool2 = Tool('榔头')
print(Tool.count)
tool3 = Tool('铁锹')
print(Tool.count)

# 知道Tool类创建了多少个对象
print('现在创建了 %d 个工具' % Tool.count)