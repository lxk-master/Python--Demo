'''
替换操作
    如果希望用新的内容替换字符串中指定的内容,可以使用replace方法
'''
s = 'hello, world'
print(s.replace('o', '@')) # hell@, w@rld     替换所有 'o' 为 '@'
print(s.replace('o','@',1)) # hell@, world.   第三个参数指定替换的次数