# 可以通过字符串的 startwith、endwith 来判断字符串是否以某个字符串开头和结尾,还可以用 is 开头的方法判断字符串的特征,这些方法都返回布尔值.
s1 = 'hello, world!'
# startwith 方法检查字符串是否以指定的字符串开头返回布尔值
print(s1.startswith('He')) # False
print(s1.startswith('hel')) # True
# endwith 方法检查字符串是否以指定的字符串结尾返回布尔值
print(s1.endswith('!')) # True


s2 = 'abc123456'
# isdigit方法检查字符串是否由数字构成返回布尔值
print(s2.isdigit()) # False
# isalpha方法检查字符串是否以字母构成返回布尔值
print(s2.isalpha()) # False
# isalnum方法检查字符串是否以数字和字母构成返回布尔值
print(s2.isalnum()) # True