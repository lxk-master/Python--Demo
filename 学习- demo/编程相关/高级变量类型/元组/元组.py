'''
元组
    元组的定义
        Tuple(元组)与列表类似,不同之处在于元组的元素不能修改
            元组表示多个元素组成的序列
            元组在Python开发中,有特定的应用场景
        用于存储一串信息,数据之间使用 , 分隔
        元组用 () 定义
        元组的索引从0开始
            索引就是元素在元组中的位置编号
        info_tuple = ('zhangsan', 18, 1.75)
        创建空元组
            info_tuple = ()
        元组中只包含一个元素时,需要在元素后面加逗号
            info_tuple = (50, )
    元组常用操作
        # 定义一个元组
        info = ()
        # 统计元组中出现的元素的次数
        info.count
        # index 指的是当前元素的下标
        info.index
    循环遍历
        取值就是从元组中获取存储在指定位置的数据
        遍历就是从头到尾依次从元组中获取数据
    元组和列表之间的转换
        使用list函数可以把元组转换成列表
        list(元组)
        使用tuple函数可以把列表转换成元组
        tuple(列表)
'''