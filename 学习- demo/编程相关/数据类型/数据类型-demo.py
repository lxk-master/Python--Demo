import sys


#整数/整形
num01 = 100
print(type(num01))
num01 = 1000000000
print(type(num01))
num01 = -100
print(type(num01))

#浮点数
num02 = 3.14
print(type(num02))
num02 = 3.12345667788899766554444
print(num02)
num02 = 0.000000000000000000000000002
print(num02)

#布尔类型
num01 = 100
if num01 > 10:
    print("这个数比10大")
else:
    print("这个数比10小")

#字符串型
str01 = "sandy"
str02 = "www.ilync.cn"
print(str01)
print(str01[0:2] + str02)
print(type(str01))

# 判断一个对象是否是某个数据类型
if isinstance(str02,(str)):
    print("是字符串")
else:
    print("不是字符串")

# 查看变量占用内存大小
print("num01占用的空间:", sys.getsizeof(num01))
print(sys.getsizeof(num02))