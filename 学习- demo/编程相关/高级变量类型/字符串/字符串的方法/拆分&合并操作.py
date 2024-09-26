'''
拆分合并操作
    可以好实用字符串的splist方法将一个字符串拆分为多个字符串(放在一个列表中),也可以使用join方法将列表中的多个字符串连接成一个字符串
'''
s = 'I love you'
words = s.split()
print(words)   # ['I', 'love', 'you' ]
print('#'.join(words)) # I#love#you

'''
需要说明的是splist方法默认使用空格进行拆分,我们也可以指定其他的字符来拆分字符串,而且还可以指定最大拆分次数来控制拆分的效果
'''
s = 'I#love#you#so#much'
words = s.split('#')
print(words) # ['I', 'love', 'you' 'so', 'much']
words = s.split('#', 3) # ['I', 'love', 'you' 'so#much']
print(words)