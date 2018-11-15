# 类定义


class Cat:

    def eat(self):
        # 此处self即为调用方法到对象的引用
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("小猫要喝水")


#创建对象
tom = Cat()
tom.name = "tom"
tom.eat()
tom.drink()
print(tom)
lazy_cat = Cat()
lazy_cat.name = "懒猫"
lazy_cat.eat()
