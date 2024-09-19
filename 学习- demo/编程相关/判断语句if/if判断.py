'''
需求
    1、定义一个整数变量记录年龄
    2、判断是否满18岁(>=)
    3、如果满18岁,允许进入网吧嗨皮
'''
# 定义年龄变量
# age = 17
# # 判断是否满18岁
# # if语句及缩进部分的代码是一个完整的代码块
# if age >= 18:
#     print("允许进入网吧嗨皮")
# else:
#     print("现在最重要的事情是学习")

# age = int(input('请输入年龄: '))
#
# if age >= 18 or age <= 20:
#     print('现在可以进入网吧happy~')
# else:
#     print('现在最重要的是学习!')

# 天气 = True
# if not  天气:
#     print('今天下雨')
# else:
#         print('今天晴天')


'''
1、定义一个整数变量age,编写代码年龄是否正确
    要求人的年龄在0-120之间
2、定义两个整数变量,python_soure、c_soure,编写代码判断成绩
    要求只要有一门成绩>60分就合格
3、定义一个布尔型变量, is_emplyee, 编写代码判断是否是本公司员工
    如果不是,提示不允许进入
'''


'''
需求
    1、定义holiday_name字符串变量记录节日名称
    2、如果是情人节应该买玫瑰/看电影
    3、如果是平安夜应该买苹果/吃大餐
    4、如果是生日应该买蛋糕
    5、其他的日子每天都是节日啊...
'''
# holiday_name = '春节'
# if holiday_name == '情人节':
#     print('买玫瑰')
#     print('看电影')
# elif holiday_name == '平安夜':
#     print('买苹果')
#     print('吃大餐')
# elif holiday_name == '生日':
#     print('买蛋糕')
# else:
#     print('每天都是节日啊...')


'''
需求
    1、定义布尔变量has_ticket表示是否有车票
    2、定义整形变量knife_length表示刀的长度,单位:厘米
    3、首先检查是否有车票,如果有才允许进行安检
    4、安检时,需要检查刀的长度,判断是否超过20厘米
        如果超过20厘米,提示刀的长度,不允许上车
        如果不超过20厘米,安检通过
    5、如果没有车票,不允许上车
'''
# has_ticket = True
# knife_length = 2
# if has_ticket:
#     print('请安检')
#     if knife_length >= 20:
#         print('安检不通过,不允许携带 %d 厘米长的刀具上车' % knife_length)
#     else:
#         print('旅途愉快~')
# else:
#     print('请购买车票!')


'''
综合应用
    需求
        1、从控制台输入要出的拳--石头(1) / 剪刀(2) / 布(3)
        2、电脑随机出拳---假定电脑只会出石头,完成整体代码功能
        3、比较胜负
            序号                      规则
            1                        石头 胜 剪刀
            2                        剪刀 胜   布
            3                        布  胜   石头
'''
import random
player = int(input('请出拳: 石头(1) / 剪刀(2) / 布(3):___'))
computer = random.randint(1, 4)
print('电脑出的是:',computer)
if  ((player == 1 and computer == 2)or
        (player ==2 and computer == 3)or
        (player ==3 and computer == 1)):
    print('电脑好菜~')
elif player == computer:
    print('心有灵犀')
else:
    print('不服!再来!')
