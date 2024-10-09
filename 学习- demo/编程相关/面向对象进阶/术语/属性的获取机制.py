'''
在Python中,属性的获取存在一个向上查找机制
要访问类属性有两种方式
    1、类名.类属性
    2、对象.类属性(不推荐)

注意
    如果使用对象.类属性 = 值 赋值语句,只会给对象添加一个属性,而不会影响到类属性的值
'''
class Tool(object):
    count = 0
    def __init__(self, name):
        self.name = name

        Tool.count += 1

tool1 = Tool('斧头')
print(Tool.count)

# 对象.类属性 不推荐
# 实例属性 分不清当前的属性是对象属性还是类属性
print(tool1.count)

# 通过对象.类属性进行重新赋值    如果当前重新赋值后会不会对当前类属性造成影响
tool1.count = 99
# 在当前对象中重新生成一个实例属性 并不是类属性
print(f'工具对象总数:{tool1.count}')

print(f'使用类.类属性输出当前类属性的值:{Tool.count}')