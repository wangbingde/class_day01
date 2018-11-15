# 面向对象封装案例1


class Person:

    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "%s体重是%s公斤" % (self.name,self.weight)

    def run(self):
        self.weight-=0.5
        print("%s每次跑步会减少0.5公斤" % self.name)

    def eat(self):
        self.weight+=1
        print("%s每次吃饭会增加1公斤" % self.name)


xiaoming = Person("小明",75.0)
print(xiaoming)
xiaoming.run()
xiaoming.eat()
print(xiaoming)
xiaomei = Person("小美",45.0)
print(xiaomei)
