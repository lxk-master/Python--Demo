'''
Python中的集合是可变类型,我们可以通过集合的方法为集合添加或删除元素
'''

# 创建一个空集合
set1 = set()

# 通过add方法添加元素
set1.add(33)
set1.add(55)
set1.update({1, 10, 100, 1000})
print(set1)

# 通过 discard 方法删除指定元素
set1.discard(1000)
set1.discard(99)
print(set1)

# 通过remove方法删除指定元素,建议先做运算再删除
# 否则元素如果不在集合中就会引发 KeyError异常
if 10 in set1:
    set1.remove(10)
print(set1) # {33, 1, 100, 55}

# pop方法可以从集合中随机删除一个元素并返回该元素
print(set1.pop())

# clear方法可以清空整个集合
set1.clear()
print(set1) # set()

# 如果要判断两个集合有没有相同的元素,可以用 isdisjoint 方法,没有相同元素返回True,否则返回False
set1 = {'Java', 'Python', 'Go', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Objective-C', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))    # False
print(set1.isdisjoint(set3))    # True