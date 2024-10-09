'''
Python为集合类型提供了非常丰富的运算符,主要包括: 成员运算、交集运算、差集运算、比较运算(相等性、子集、超集等)
'''

# 成员运算
#   可以通过成员运算 in 和not in 检查元素是否在集合中
set1 = {11, 12, 13, 14, 15}
print(10 in set1) # False
print(15 in set1) # True
set2 = {'Python', 'Java', 'Go', 'Swift'}
print('Ruby' in set2) # False
print('Java' in set2) # True

# 交并差运算
# Python中的集合跟数学的集合一样,可以进行交集、并集、差集运算,而且可以通过运算符和方法调用两种方式来进行操作
set1 = {1,2,3,4,5,6,7}
set2 = {2,4,6,8,10}
# 交集
# 方法一: 使用 & 运算符
print(set1 & set2) # {2, 4, 6}
# 方法二: 使用intersection方法
print(set1.intersection(set2)) # {2, 4, 6}

# 并集
# 方法一: 使用 | 运算符
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# 方法二: 使用 union 方法
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
# 方法一: 使用 - 运算符
print(set1 - set2) # {1, 3, 5, 7}
# 方法二: 使用 difference 方法
print(set1.difference(set2)) # {1, 3, 5, 7}
print(set2.difference(set1)) # {8, 10}

# 对称差
# 方法一: 使用 ^ 运算符
print(set1 ^ set2) # {1, 3, 5, 7, 8, 10}
# 方法二: 使用symmetric_difference方法
print(set1.symmetric_difference(set2)) # {1, 3, 5, 7, 8, 10}
# 方法三: 对称差相当于两个集合的并集减去交集
print((set1 | set2) - (set1 & set2)) # {1, 3, 5, 7, 8, 10}