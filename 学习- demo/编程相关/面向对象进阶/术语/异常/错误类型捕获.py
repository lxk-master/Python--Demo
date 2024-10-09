'''
在程序执行时,可能会遇到不同类型的异常,并且需要针对不同类型的异常,做出不同的响应,此时,就需要捕获错误类型了
单Python解释器抛出异常时,最后一行错误信息的第一个单词,就是错误类型
'''



try:
    num = int(input('请输入一个整数: '))
    result = 8 / num
    print(result)
except ValueError:
    print('请输入一个正确的整数')
except ZeroDivisionError:
    print('除0错误')




'''
错误分为很多种
    ValueError  值错误
    ZeroDivisionError   分母不能为0
'''
# num = int(input('请输入一个整数: '))
# result = 8 / num
# print(num)