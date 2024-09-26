# 函数的嵌套调用
def demo_test1():
    print('*' * 50)
    print('test 1')
    print('*' * 50)

def demo_test2():
    print('-' * 50)
    print('test 2')
    demo_test1()
    print('-' * 50)

# demo_test2()





# 需求1
# 定义一个 print_line 函数,能够打印 * 组成的分割线

def print_line():
    print('*' * 50)
print_line()

# 需求2
# 可以打印任意字符的分割线函数
def print_line_1(char):
    print(char * 50)
print_line_1('-')

# 定义一个函数能够打印任意重复次数的分割线
def print_line_2(char,num):
    print(char * num)
print_line_2('%', 10)

# 需求4 定义一个函数能够打印5行分割线 分割线要求要符合需求3
def print_line_3(char, num):
    print(char * num)

def print_line_4(char, num):
    row = 0
    while row < 5:
        print_line_3(char, num)
        row += 1
print_line_4('*', 30)