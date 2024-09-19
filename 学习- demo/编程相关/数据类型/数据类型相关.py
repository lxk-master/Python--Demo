'''
数据类型
    整形
        int  如: 100, -1
    浮点型
        float  如: 3.14, -94.7.   默认保留17位数,如果小数点后数值较长会用科学计数法表示,如0.0000000000000002此种
    布尔型
        bool  如: False, True     一般用来做判断,也可以参与计算(False为0 True为1)
    字符串型
        str  如: “iLync”, “你好 ! 中国”
        
获取数据类型
    num01 = 100
    print(type(num01))

判断一个对象是否是某个数据类型
if isinstance(str02,(str)):
    print("是字符串")
else:
    print("不是字符串")

查看变量所占内存空间大小
    num02 = 100
    print(sys.getsizeof(num02))
'''