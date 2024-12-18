'''
单继承
多继承
面向对象三大特性:
    1、封装根据职责讲属性和方法封装到一个抽象的类中
    2、继承实现代码的重用,相同的代码不需要重复的编写
    3、多态不同的对象调用相同的方法,产生不同的执行结果,增加代码的灵活度
'''


'''
单继承
    继承的概念:
        子类拥有父类所有的方法和属性
    
    继承的语法:
        class 类名(父类名):
            pass
        子类继承自父类,可以直接享用父类中已经封装好的方法,不需要再次开发
        子类中应该根据职责,封装子类特有的属性和方法
    
    专业术语(名称参照案例)
        Dog类是Animal类的子类,Animal类是Dog类的父类,Dog类从Animal类继承
        Dog类是Animal类的派生类,Animal类是Dog类的基类,Dog类从Animal类派生
        
    继承的传递性
        C类从B类继承,B类又从A类继承
        那么C类就具有B类和A类的所有属性和方法
        子类拥有父类以及父类的父类中封装的所有属性和方法    
'''