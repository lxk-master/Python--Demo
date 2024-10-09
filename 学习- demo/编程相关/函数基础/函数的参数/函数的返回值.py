def sun_2_num(num1, num2):
    return num1 + num2
# 我们可以使用一个变量进行函数返回值的接收
res = sun_2_num(20, 30)
print('计算结果: %d' % res)

# 在函数中使用 return 后续的代码是不会被执行的 return代表当前函数已经执行完毕