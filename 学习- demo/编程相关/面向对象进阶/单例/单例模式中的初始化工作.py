'''
只执行一次初始化工作
    在每次使用类名()创建对象时,Python的解释器都会知道调用两个方法:
        __new__ 分配空间
        __init__ 对象初始化
    对new方法改造之后,每次都会得到第一次被创建对象的引用
    但是,初始化方法还会被再次调用

需求:
    让初始化动作只被执行一次
解决办法
    1、定义一个类属性 init_flag标记是否执行过初始化动作,初始值为False
    2、在__init__方法中判断init_flag,如果为False,就执行初始化动作
    3、然后将init_flag设置为True
    4、这样再次自动调用__init__方法时,初始化动作就不会再次执行了
'''


class MusicPlayer:
    # 创建类属性
    instance = None

    # 创建一个用于记录 init函数的执行次数的类属性
    init_flag =  False

    def __new__(cls, *args, **kwargs):
        # 1.当前类属性是否是一个空对象
        if cls.instance is None:
            # 2.调用父类new方法
            cls.instance = super().__new__(cls)
        # 3.返回被更改的类属性
        return cls.instance

    # 初始化方法
    def __init__(self):
        # 1.判断init是否第一次执行
        if MusicPlayer.init_flag:
            # 如果执行return 那么下面的代码全部都不执行
            return
        print('初始化播放器...')

        # 2. 如果执行了一次初始化方法之后需要修改类属性中的值
        MusicPlayer.init_flag = True


# 创建多个对象
player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1)
print(player2)