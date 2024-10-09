class Student:
    """学生"""
    # 初始化方法,给当前对象创建属性
    def __init__(self, name, age):
        """初始化方法"""
        # 给当前类添加属性
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        # 属性使用 self 进行调用 参数是直接调用
        print(f'{self.name},年龄{self.age},正在学习{course_name}.')

    def play(self):
        print(f'{self.name},年龄{self.age},正在玩游戏')

# 实例化类
stu1 = Student('顾安', 18)
stu1.study('Python 程序设计')

stu2 = Student('夏洛', 20)
stu2.play()