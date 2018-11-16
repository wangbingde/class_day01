# 封装案例3


class Gun:

    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count
        print("子弹数量%s" % self.bullet_count)

    def shoot(self):
        if self.bullet_count <= 0:
            print("子弹不足")
            return
        self.bullet_count -= 1
        print("射出子弹,剩余%s" % self.bullet_count)


class Solider:

    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("没有枪")
            return
        print("射击")
        self.gun.shoot()


ak = Gun("ak47")
ak.shoot()
xu = Solider("许三多")
print(xu.gun)
# print(xu)
xu.gun = ak
# print(xu)
print(xu.name)
print(xu.gun.model)
xu.gun.add_bullet(40)
xu.fire()
