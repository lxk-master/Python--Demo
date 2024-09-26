'''
需求
    1、编写一个打招呼 say_hello 的函数,封装三行打招呼的代码
    2、在函数下方调用打招呼的代码
'''

name = '小明'

# 解释器知道这里定义了一个函数
def say_hello():
    '''
    当前函数完成打招呼的功能
    :return:
    '''
    print('hello 1')
    print('hello 2')
    print('hello 3')
print(name)
# 只有在调用时,之前定义的函数才会执行
# 函数执行完成之后,会重新回到之前的程序中,继续执行后续的代码
# 调用函数
say_hello()
print(name)