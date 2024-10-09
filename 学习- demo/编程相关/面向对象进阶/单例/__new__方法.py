'''
使用类名()创建对象时,Python的解释器首先会调用 __new__ 方法为对象分配空间
__new__ 是一个由object基类提供的内置的静态方法,主要作用有两个:
    在内存中为对象分配空间
    返回对象的引用
Python的解释器获得对象的引用后,将引用作为第一个参数,传递给 __init__ 方法

重写 __new__ 方法的代码非常固定
    重写__new__方法一定要return super().__new__(cls)
    否则Python的解释器得不到分配了空间的对象引用,就不会调用对象的初始化方法
    注意: __new__ 是一个静态方法,在调用时需要主动传递cls参数
'''

# 需要创建一个音乐播放器
class MusicPlayer:
    # 创建new方法
    '''
    当我们调用new方法之后,需要在当前的new方法中调用父类的new方法
        object
            父类的new方法已经实现了划分内存地址的代码
            在内存中并没有划分空间给当前类
    '''
    def __new__(cls, *args, **kwargs):
        print('创建对象, 分配空间')

        # 为对象分配空间 父类中的new方法是一个类方法
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print('播放器初始化')

# 创建播放器对象
player = MusicPlayer()

# 打印当前类对象地址
print(player)