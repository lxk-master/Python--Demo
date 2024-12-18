'''
异常的传递--当函数/方法执行出现异常,会将异常传递给函数/方法的调用一方
如果传递到主程序,仍然没有异常处理,程序才会被终止

提示
    在开发中,可以在主函数中增加异常捕获
    而在主函数中调用的其他函数,只要出现异常,都会传递到主函数的异常捕获中
    这样就不需要在代码中,增加大量的异常捕获,能够保证代码的整洁
'''

def demo1():
    #try:
    return int(input('输入整数: '))
    # except:
    #     print('出现错误')

def demo2():
    return demo1()

# 在主程序中添加异常
'''
可以提高代码的简洁性
'''
if __name__ == '__main__':
    try:
        print(demo2())
    # 如果在调用函数的时候不知道错误类型 使用错误基类
    except Exception as e:
        print('未知错误: %s' % e)