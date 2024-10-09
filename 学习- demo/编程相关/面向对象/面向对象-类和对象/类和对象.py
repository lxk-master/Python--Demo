'''
定义了一个学生类
    有定义方法
    每一位学生的行为都是不一样的
'''
class student:
    # 如果函数在类中,那么被称之为方法
    def study(self,coure_name):
        print(f'学生正在学习{coure_name}.')

    def play(self):
        print('学生正在玩游戏.')


# 当前的stu1 是 student这个类的对象 是一个具体的实例
stu1 = student()
stu2 = student()
# 当前输出的值为这个具体实例在内存中的地址,十六进制的值
# print(stu1)
# print(stu2)
# # 内存中的地址转十进制
# print(id(stu1), id(stu2))
# # 通过hex参数转回十六进制
# print(hex(id(stu1)), hex(id(stu2)))

# 通过 对象.方法去调用类中的方法
stu1.study('Python 程序设计')
# 需要对当前的类进行实例化
# student.study('Java 程序设计')
student().study('Java 程序设计')

'''
想要去调用当前类中的方法
    首先要对当前类进行实例化
'''