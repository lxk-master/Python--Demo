'''
修剪操作
    字符串的strip方法可以帮我们获得原字符串修剪掉左右两端空格之后的字符串,这个方法非常有实用价值,通常用来将用户输入因为不小心键入的头尾空格去掉,
    strip方法还有lstrip和rstrip两个版本(删除字符串左边和右边的空格)
'''
s = '  tuling_puthon@123.com \t\r\n'
# striip方法修剪字符串两端左右两侧空格之后的字符串
print(s.strip()) #   tuling_python@123.com

