# 私有属性和私有方法


class Woman:

    def __init__(self,name):
        self.name=name
        self.__age = 18

    def __secret(self):

        print("%s的年龄是%d" % (self.name,self.__age))


xiao = Woman("小芳")
print(xiao.name)
#xiao.secret()
xiao._Woman__secret()
