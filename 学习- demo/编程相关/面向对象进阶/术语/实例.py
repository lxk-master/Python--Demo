'''
1、使用面向对象开发,第一步是设计类
2、使用类名创建对象,创建对象的动作有两步
    1)在内存中为对象分配空间
    2)调用初始化方法 __init__ 为对象初始化
3、对象创建后,内存中就有了一个实实在在的对象---实例

1、创建出来的对象叫做类的实例
2、创建对象的动作叫做实例化
3、对象的属性叫做实例属性
4、对象调用的方法叫做实例方法

在程序执行时
    1、对象各自拥有自己的实例属性
    2、调用对象的方法可以通过self.
        访问自己的属性
        调用自己的方法

结论:
    每一个对象都有自己独立的内存空间,保存各自不同的属性
    多个对象的方法,在内存中只有一份,在调用方法时,需要把对象的引用传递到方法内部
'''