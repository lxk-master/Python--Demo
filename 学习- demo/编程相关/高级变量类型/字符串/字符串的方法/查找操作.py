s = 'hello, world!'

# find 方法从字符串中查找另一个字符串所在的位置
# 找到了返回字符串中另一个字符串首字符的索引
print(s.find('or')) # 8
# 找不到返回 -1
print(s.find('shit')) # -1

# index方法与find方法类似
# 找到了返回字符串中另一个字符串首字母的索引
print(s.index('or')) # 8
# 找不到引发异常
#print(s.index('shit')) # ValueError: substring not found


# 在使用 find和index方法时还可以通过方法的参数来指定查找的范围,也就是查找不必从索引为0的位置开始.
# find和index方法还有逆向查找(从后向前查找),分别是rfind和rindex.

s1 = 'hello good world!'
# 从前向后查找字符 o 出现的位置(相当于第一次出现)
print(s1.find('o')) # 4
# 从索引为5的位置开始查找字符 o 出现的位置
print(s1.find('o', 5)) # 7
# 从后向前查找字符 o 出现的位置(相当于最后一次出现)
print(s1.rfind('o')) # 12