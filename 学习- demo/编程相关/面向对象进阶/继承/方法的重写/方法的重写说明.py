'''
子类拥有父类所有的方法和属性
子类继承自父类,可以直接享受父类中已经封装好的方法,不需要再次开发

当父类的方法实现不能满足子类需求时,可以对方法进行重写(override)

重写父类有两种情况
    1、覆盖父类的方法
        如果在开发中,父类的方法实现和子类的方法实现完全不同,就可以使用覆盖的方式,在子类中重新编写父类的方法实现
            具体的实现方式,就相当于在子类中定义了一个和父类同名的方法并且实现
    2、对父类方法进行扩展
        如果在代码开发中,子类的方法实现中包含父类方法的实现
            父类原本封装的方法实现是子类方法的一部分
            就可以使用扩展的方式
                1、在子类中重写父类的方法
                2、在需要的位置使用 super().父类方法 来调用父类方法的执行
                3、代码其他位置针对子类的需求,编写子类特有的代码实现

                关于super
                    在Python中super是一个特殊的类
                    super() 就是使用super()类创建出来的对象
                    最常使用的场景就是在重写父类方法时,调用父类中封装的方法实现

                调用父类方法的另外一种方式(Python2.x)
                    父类名.方法(self)
                    目前Python3.x还支持这种方式
                    这种方法不推荐,因为父类一旦发生变化,方法调用位置的类名同样需要修改

                提示
                    在开发时,父类名和 super() 两种方式不要混用
                    如果使用当前子类名调用方法,会形成递归调用,出现死循环
'''