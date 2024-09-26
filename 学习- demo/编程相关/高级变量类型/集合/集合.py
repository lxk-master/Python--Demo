'''
常用数据类型之集合
    与列表和元组一样为容器型的数据类型-集合(set)
    特性:
        在数学课本的定义为“把一定范围的、确定的、可以区别的事物当成一个整体来看待”,集合中的事物通常称为集合的元素,集合应满足以下特性:
            1、无序性: 在一个集合中,每个元素的地位都是相同的,元素之间是无序的.
            2、互异性: 一个集合中,任何两个元素都是不相同的,即元素在集合中只能出现一次.
            3、确定性: 给定一个集合和一个任意元素,该元素要么属于这个集合,要么不属于这个集合,二者必居其一,不允许有模棱两可的情况出现.
    Python中程序的集合跟数学的集合是完全一致的,需要强调的是,上面所说的无序性和互异性.
    无序性说明集合中的元素并不像列中的元素那样一个挨着一个,可以通过索引实现随机访问(随机访问指的是给定一个有效的范围,随机抽取一个数字,然后通过这个数字可以获取到对应的元素)
    所以Python中的集合肯定不能够支持索引运算.
    另外,集合的互异性决定了集合中不能有重复元素,这一点也是集合区别于列表的关键,说的更直白一些就是,Python中的集合类型会对其中的元素做去重处理.
    Python中的集合一定是支持 in 和 not in 成员运算的,这样就可以确定一个元素是否属于集合,也就是上面所说的集合的确定性.
    集合的成员运算在性能上要优于列表的成员运算,这事集合的底层存储特性(哈希存储)决定的.
'''