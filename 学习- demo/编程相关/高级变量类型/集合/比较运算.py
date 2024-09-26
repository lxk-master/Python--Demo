f'''
两个集合可以用 == 和 != 进行相等性判断,如果两个集合中的元素完全相同,那么 == 比较的结果就是True,否则就是False.
如果集合A中的任意一个元素都是集合B的元素,那么集合A称为集合B的子集,
A是B的子集,反过来讲也可以称B是A的超集,如果A是B的子集且A不等于B,那么A就是B的真子集
'''

set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = set2
# < 运算符表示真子集, <= 运算符表示子集
print(set1 < set2, set1 <= set2)  # True True
print(set2 < set3, set2 <= set3)  # False True
# 通过 issubset 方法也能进行子集判断
print(set1.issubset(set2))  # True
# 反过来也可以也可以用 issuperset 或 > 运算符进行超集判断
print(set2.issuperset(set1))    # Ture
print(set2 > set1)  # True