'''
单例--让类创建的对象,在系统中,只有唯一的一个实例
    1、定义一个类属性,初始值是None,用于记录单例对象的引用
    2、重写__new__方法
    3、如果类属性 is None,调用父类方法分配空间,并在类属性中记录结构
    4、返回类属性中记录的对象引用
'''


class MusicPlayer:
    # 类属性 用来记录当前创建的类对象的引用地址的
    instace = None

    # 重写new方法 new方法作用:为类创建内存空间
    def __new__(cls, *args, **kwargs):
        # 1.判断当前类属性是否为None 如果是第一次执行当前的这个类,那么类属性为None
        if cls.instace is None:
            # 2. 调用父类方法 类对象创建一个内存空间
            cls.instace = super().__new__(cls)
        # 3. 返回类属性保存的对象引用
        return cls.instace

# 创建类对象 内存不一样的 证明当前两个类对象是两个独立的对象
player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1)
print(player2)