def sum_2_num():
    '''
    定义一个函数sum_2_num
    :return:
    '''
    num1 = 10
    num2 = 20
    result = num1 + num2
    '''
    完成变量的赋值
    '''
    print("%d + %d = %d" % (num1, num2, result))
sum_2_num()


'''
需求
    用户可以随意传入两个值
    针对两个值进行计算
'''
def sum_2_num_1(num1,num2):
    result = num1 + num2
    print('%d + %d = %d' % (num1, num2, result))
sum_2_num_1(50,20)