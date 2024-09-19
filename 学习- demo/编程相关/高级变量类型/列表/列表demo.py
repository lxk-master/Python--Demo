# 定义一个列表
name_list = ['张三', '李四', '王五']
print(name_list)

# 在指定位置插入数据
name_list.insert(0, '夏洛')
print(name_list)
name_list.insert(2, '顾安')
print(name_list)

# 在列表末尾添加一条数据
name_list.append('大海老师')
print(name_list)

# extend 添加一个列表
test_1 = [1, 2, 3]
test_2 = [4, 5, 6]
test_1.extend(test_2)
print(test_1)

# 在指定位置修改元素数据
name_list[1] = '木木'
print(name_list)

# 删除指定数据
del name_list[4]
print(name_list)

# 删除列表中出现的第一个数据
name_list.append('李四')
print(name_list)
name_list.remove('李四')
print(name_list)

# pop删除
name_list.pop()
print(name_list)
name_list.pop(0)
print(name_list)

# 清除整个列表
# name_list.clear()
# print(name_list)

# 统计    索引计数从0开始,列表长度计算从1开始
print(len(name_list))

# 统计列表中元素出现的次数
name_list.append('木木')
print(name_list)
print(name_list.count('木木'))

# 列表排序
# 升序
number_list = [2, 1, 5, 3, 7, 9]
number_list.sort()
print(number_list)

# 降序
number_list.sort(reverse=True)
print(number_list)

# 逆序
number_list.reverse()
print(number_list)

# 循环取值
print(number_list)
for i in number_list:
    print(i)
    print(type(i))

for i in name_list:
    print(i)
    print(type(i))