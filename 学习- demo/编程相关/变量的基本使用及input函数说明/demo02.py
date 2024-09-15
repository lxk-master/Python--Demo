name = '小明'
print('我的名字叫%s, 请多多关照' % name)

stu_number = 123
print('我的学号是: %d' % stu_number)

# python 内置的input函数保存的默认类型为字符串
price = float(input('苹果的单价为: '))
weight = float(input('苹果的重量为: '))

money = price * weight
print('当前苹果的单价为: %.2f, 重量为: %.2f, 总价为: %.2f' % (price, weight, money))

scale = 10.23
print('数据的输出比例是 %.02f%%' % (scale * 100))