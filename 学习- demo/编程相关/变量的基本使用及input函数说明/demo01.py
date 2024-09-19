# from distutils.log import fatal
#
# from numpy.core.defchararray import rpartition
# from spacy.symbols import number
#
# qq_number = 1234567
# qq_password = 123
#
# print(qq_number)
# print(qq_password)
#
# # 价格
# price = 8.5
#
# # 定义购买重量
# weight = 7.5
#
# # 总金额
# # money = price * weight
# money = price * weight -5
#
# # 如果只买苹果,那么返还5元
# print(money)
#
#
# # 小明的个人信息
# # 姓名
# name = '小明'
# # 年龄
# age = 18
# # 性别 类型为bool类型 有两个值 True 和 False  是与否
# sex = True
# # 身高
# height = 1.75
# # 体重
# weight = 75.0
#
# # 字符串使用 + 进行字符串拼接
# first_name = "小"
# last_name = "明"
# print(first_name + last_name)
#
# number_data = 10
# # print(first_name + number_data)
#
#
# # 使用input函数进行变量输入
# data = input('请输入一个数字: ')
# print(data)


# 输出苹果的单价
price_str = input('请输入苹果单价: ')
# 要求苹果重量
weight_str = input('请输入苹果的重量: ')
# 计算金额
    # 将苹果单价转换成小数
price = float(price_str)
    # 将苹果重量转换为小数
weight = float(weight_str)
# 计算付款金额
money = price * weight
# 当前的变量类型为浮点数(小数)
print(money)