# 面向对象案例2


class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s的占地面积是%.2f平米" % (self.name, self.area)


class House():

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        print("房子的类型是%s" % self.house_type)
        print("总面积是%.2f平米" % self.area)
        print("剩余面积是%.2f平米" % self.free_area)
        return "家具列表：%s" % self.item_list

    def add_item(self, item):
        print("-"*50)
        if item.area <= self.free_area:

            print("添加%s占地%.2f平米" % (item.name,item.area))
            self.free_area -= item.area
            self.item_list.append(item.name)
        else:
            print("不能添加%s" % item.name)
            return


my_house = House("两室一厅", 60)
print(my_house)
bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜",20)
table = HouseItem("餐桌",1.5)
print(bed)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)
print(my_house)
