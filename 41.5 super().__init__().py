"""Python中子类会继承父类所有的类属性和类方法"""
"""严格来说 类的构造方法其实就是实例方法 因此 父类的构造方法 子类同样会继承"""

"""Python支持多继承的面向对象编程语言 如果子类继承的多个父类中包含同名的实例方法
   则子类对象在调用该方法时 会优先选择排在最前面的父类中的实例方法 构造方法也是如此"""

"""http://c.biancheng.net/view/2290.html"""

# 举个例子


class People:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("我是人，名字为", self.name)


class Animal:
    def __init__(self, food):
        self.food = food

    def display(self):
        print("我是动物，我吃", self.food)

# People中的name属性和say()会屏蔽Animal中的


class Person(People, Animal):
    pass


per = Person("Zhangsan")
per.say()  # 运行结果：我是人，名字为Zhangsan
# per.display() 这个运行则会报错

"""Person类同时继承People和Animal 因为People在前
   即在创建per对象时 将会调用从People继承来的构造函数"""
"""因此 在创建per对象时 还要给name属性进行赋值"""

"""正确的做法是 定义子类自己的构造方法
   等同于重写第一个直接父类的构造方法
   如果在子类中定义构造方法 则必须在该方法中调用父类的构造方法"""

"""在子类中的构造方法中 调用父类构造方法的方式有2种"""

"""类可以看做一个独立空间 在类的外部调用其中的实例方法 可以向调用普通函数那样
   只不过需要额外备注类名（此方式又称为未绑定方法）"""

"""使用 super() 函数 super().__init__(self,...)
   但如果涉及多继承 该函数只能调用第一个直接父类的构造方法
   而调用其它父类构造方法的方式只能使用未绑定方法"""

# 更改后的函数


class newPerson(People, Animal):
    # 自定义构造方法
    def __init__(self, name, food):
        # 调用people类的构造方法
        super().__init__(name)  # 等于 super(People,self).__init__(name)
        # People.__init__(self,name) 使用未绑定方法调用People类构造方法
        # 调用其他父类的构造方法 需要手动给self传值
        Animal.__init__(self, food)


newPer = newPerson("Zhangsan", "熟食")
newPer.say()
newPer.display()

"""Person 类自定义的构造方法中 调用 People 类构造方法 可以使用 super() 函数
   也可以使用未绑定方法 但是调用 Animal 类的构造方法 只能使用未绑定方法"""
