# 定义一个元组
info_data = (1, 'zhangsan', 1.43)
print(type(info_data))
info_data_1 = ()
print(type(info_data_1))

# 在声明元组时,如果元组中的值只有一个,那么必须在这个值的后面添加逗号
info_data_2 = (1,)
print(type(info_data_2))

# 统计元组中出现的元素的次数
info_data = (1, 1, 2, 4, 5, 1)
print(info_data.count(1))

# index 指的是当前元素的下标
print(info_data.index(4))

# 遍历
for i in info_data:
    print(i)

print(type(info_data))
print(type(list(info_data)))
print(type(tuple(info_data)))