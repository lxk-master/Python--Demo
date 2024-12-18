class Student:
    """学生"""

    def __init__(self,name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self,course_name):
        """学习"""
        print(f'({self.name}正在学习{course_name}.)')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')

    # 使用类中内置的魔术方法来实现
    def __repr__(self):
        return f'{self.name}: {self.age}'


stu1 = Student('顾安', 40)
print(stu1)
students = [stu1, Student('李元芳', 36), Student('王大锤', 25)]
print(students)