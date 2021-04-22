
# !!!!!!!!!!!!!!!!!!!상속!!!!!!!!!!!!!!!!!!!!!!!!!

class Person:
    # 멤버변수
    name = ""
    age = 0

    # 멤버메서드

    def eat(self):
        print('먹다')

    def __str__(self):
        return self.name + ' ' + str(self.age)

class Man(Person):
    speed = 0

    def run(self):
        print('빨리 달리다')

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' ' + str(self.speed)


class SuperMan(Man):
    fly = False

    def sky(self):
        print('하늘을 날다.')

    def __str__(self):
        return self.name + ' ' + \
               str(self.age) + ' ' + \
               str(self.speed) + ' ' + \
               str(self.fly)