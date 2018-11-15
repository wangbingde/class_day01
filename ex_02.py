# 初始化方法


class Cat:

    def __init__(self,new_name):
        print("初始化方法")
        self.name = new_name

    def __del__(self):
        print("对象销毁")

    def __str__(self):
        return "我是小猫%s" % self.name


# tom是一个全局变量，所有程序运行结束后才会删除
tom=Cat("Tom")
print(tom.name)
lazy_cat = Cat("懒猫")
print(lazy_cat.name)
print(tom)
#del关键字可以删除一个对象
del lazy_cat
print("-" * 50)