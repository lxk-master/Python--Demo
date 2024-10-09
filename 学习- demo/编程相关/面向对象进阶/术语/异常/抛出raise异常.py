'''
应用场景
    在开发中,除了代码执行出错 Python解释器会抛出异常之外
    还可以根据应用程序特有的业务需求主动抛出异常

抛出异常
    在Python中提供了一个Exception异常类
    在开发时,如果满足特定业务需求时,希望抛出异常,可以:
        1、创建一个Exception的对象
        2、使用raise关键字抛出异常
'''

def input_password():
    # 1.提示用户输入密码
    pwd = input('请输入密码: ')

    # 2.判断用户输入的密码是否满足长度要求
    if len(pwd) >= 8:
        return pwd

    # 3.如果用户输入的密码不满足长度要求 这创建异常并抛出异常
    print('主动抛出异常')
    # 自定义错误
    ex = Exception('密码长度不足')

    # 4.主动抛出异常
    raise ex

# 在主函数中捕获异常
if __name__ == '__main__':
    try:
        print(input_password())
    except Exception as e:
        print(e)