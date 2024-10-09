'''
Python 中除了字符串str类型外,还有一种表示二进制数据的字节串类型(bytes).
所谓字节串,就是由零个或多个字节组成的有限序列.
通过字符串 encode 方法,我们可以按照某种编码方式将字符串编码为字节串.
我们也可以使用字节串 decode 方法,将字节串解码为字符串
'''
a = '顾安'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b, c) # b'\xe9\xa1\xbe\xe5\xae\x89'   b'\xb9\xcb\xb0\xb2'
print(b.decode('utf-8'))
print(c.decode('gbk'))