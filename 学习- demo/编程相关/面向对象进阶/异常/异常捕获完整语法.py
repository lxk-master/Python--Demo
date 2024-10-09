try:
    num = int(input('请输入一个整数: '))
    result = 8 / num
    print(result)
except ValueError:
    print('出现错误')
except ZeroDivisionError:
    print('除0错误')
else:
    # 如果当前代码执行成功则执行else之下的代码
    print('运算成功')
finally:
    # 当前代码无论是否执行错误,都会执行这段语句
    print('无论是否执行成功,都执行这段语句...')