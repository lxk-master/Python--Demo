# 打印5遍 hello world
# 定义重复次数的计数器
# i = 1
# # 使用while判断条件   当 i <= 5 时,重复执行循环内的代码
# while i <= 5:
#     # 要重复执行的代码
#     print('hello world')
#     # 处理计数器 i   用来结束循环,使 i > 5 使while循环的条件不成立
#     i += 1
# print('循环结束后的 i = %d' % i)
from pycparser.ply.yacc import resultlimit

# 死循环
# i = 0
# while True:
#     i += 1
#     print('这事一个死循环: %d' % i)

# 需求:   计算0-100之间所有数字的累计求和结果
# 定义最终结果的变量
# result = 0
# # 定义一个整数的变量记录循环次数
# i = 0
# # 开始循环
# while i <= 100:
#     print(i)
#     # 每一次循环,都让result这个变量和 i 这个计数器相加
#     result += i
#     # 处理计数器
#     i += 1
# print('0-100之间数字等求和结果= %d' % result)

# 需求 --- 计算0-100之间偶数的累计求和结果
# 最终结果
# resulet = 0
# # 计数器
# i = 0
# # 开始循环
# while i <= 100:
#     # 判断偶数
#     if i % 2 == 0:
#         print(i)
#         resulet += i
#     # 处理计数器
#     i += 1
# print('0-100之间偶数求和结果为: %d' % resulet)

# break 在循环过程中,如果某一个条件满足时,不希望循环继续执行
# i = 0
# while i < 10:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# print('over')

# continue 在循环过程中,如果一个条件满足后,不希望执行循环代码,但又不希望退出循环
#          也就是在整个循环中,只有某些条件,不需要执行循环代码,而其他条件都需要执行
# i = 0
# while i < 10:
#     # 当i==7时,不希望执行需要重复的代码
#     if i == 7:
#         # 在使用continue之前,同样应该修改计数器
#         # 否则会出现死循环
#         i += 1
#         # break 打印到6会终结
#         #break
#         # continue 会跳过当前if循环所指定的 i == 7 继续执行
#         continue
#     # 重复执行的代码
#     print(i)
#     i += 1




# 在控制台连续输出5行*, 每一行*数量依次递增
# row = 1
# while row <= 5:
#     print('*' * row)
#     row += 1

'''
使用循环嵌套打印小星星
    知识点: 对print函数做一个增强
        1、在默认情况下,print函数输出内容之后,会自动在内容末尾增加换行
        2、如果不希望末尾增加换行,可以在print函数输出的内容之后加, end=""
        3、其中“”中间可以指定print函数输出内容之后,继续希望显示的内容
            语法格式如下:
                # 向控制台输出内容结束之后不会换行
                print("*",end="")
                # 单纯的换行
                print("")
'''
# row = 1
# while row <= 5:
#     # 假设python没有提供字符串*操作
#     # 在循环内部,再增加一个循环,实现每一行星星打印
#     col = 1
#     while col <= row:
#         print("*", end="")
#         col += 1
#     # 每一行星号输出完成后,再增加一个换行
#     print("")
#     row += 1


# 循环嵌套: 九九乘法表

# 定义起始行
row = 1
# 最大打印9行
while row <= 9:
    # 定义起始列
    col = 1
    # 最大打印col列
    while col <= row:
        # end=“”,表示输出结果后不换行
        # “\t”可以在控制台输出一个制表符,协助在输出文本时对齐
        print("%d * %d = %d" % (col, row, row * col), end="\t")
        # 列数 + 1
        col += 1
    # 一行打印完成的换行
    print("")
    # 行数 + 1
    row += 1
    