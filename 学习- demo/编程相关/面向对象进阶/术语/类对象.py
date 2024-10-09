'''
类是一个特殊的对象
Python中,一切皆对象:
    class AAA:  定义的类属于类对象
    obj1 = AAA()    属于实例对象

在程序运行时,类同样会被加载到内存
在Python中,类是一个特殊的对象--类对象
在程序运行时,类对象在内存中只有一份,使用一个类可以创建出很多个对象实例
除了封装实例的属性和方法外,类对象还可以拥有自己的属性和方法
    1、类属性
    2、类方法
    通过类名. 的方式可以访问类的属性或者调用类的方法
        类名.属性-----类属性
        类名.方法名()-----类方法(cls)
        类名()----- __init__ 定义实例属性
        对象名.方法名()----- 实例方法(self)
'''


'''
1. 类属性（Class Attribute）

类属性是直接绑定到类上的属性，所有实例共享这一属性。它在类定义中声明，而不是在实例初始化方法（如 __init__）中声明。
所有实例都能访问类属性，并且修改类属性会影响所有实例。

关键点：
	•	species 是类属性，属于 Dog 类，而不是任何一个具体的实例。
	•	修改类属性 Dog.species 会影响所有实例，因为类属性是共享的。
'''
class Dog:
    # 类属性
    species = "Canine"

    def __init__(self, name):
        # 实例属性
        self.name = name

# 创建两个实例
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# 访问类属性
print(dog1.species)  # 输出：Canine
print(dog2.species)  # 输出：Canine

# 修改类属性
Dog.species = "Wolf"

# 再次访问类属性
print(dog1.species)  # 输出：Wolf
print(dog2.species)  # 输出：Wolf


'''
2. 类方法（Class Method）

类方法是绑定到类而不是实例的方法，类方法的第一个参数通常是 cls，表示类本身，而不是实例。类方法可以通过类或实例调用，
但它们只能访问类属性，不能直接访问实例属性。
类方法通过 @classmethod 装饰器定义。
'''
class Dog:
    species = "Canine"  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性

    # 类方法
    @classmethod
    def get_species(cls):
        return cls.species

# 通过类调用类方法
print(Dog.get_species())  # 输出：Canine

# 通过实例调用类方法
dog1 = Dog("Buddy")
print(dog1.get_species())  # 输出：Canine

# 修改类属性
Dog.species = "Wolf"
print(Dog.get_species())  # 输出：Wolf

'''
关键点：

	•	类方法使用 @classmethod 装饰器，并且第一个参数是 cls，指代类本身。
	•	类方法可以通过类名或实例调用，但它们主要用于访问和修改类属性，而不是实例属性。

类属性 vs 实例属性：

	•	类属性是所有实例共享的，全局性数据，每个实例访问到的是同一个值。
	•	实例属性是每个实例独有的，每个实例有自己的独立属性，不同实例之间的值可以不同。

类方法 vs 实例方法：

	•	类方法操作的是类本身，可以访问和修改类属性，不能直接操作实例属性。
	•	实例方法是绑定到实例的方法，操作的是实例属性，通过 self 参数访问实例数据。

3. 什么时候使用类属性和类方法？

	•	类属性适合用于描述类本身的共性，如物种名称、默认配置等。
	•	类方法适合用于执行与类相关的操作，比如创建实例、修改类属性、或者为整个类提供一些通用功能。

总结：

	•	类属性：是类本身的属性，所有实例共享它。
	•	类方法：是针对类本身的方法，用来操作类属性或进行与类相关的操作。
'''