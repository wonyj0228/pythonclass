from classmake.person_module import *

# import를 단축키(allyias..?)로 쓰는 방법
import classmake.everyday as my

day5 = my.Day('잠',10,'영등포')
print(day5)

super_man = SuperMan()
super_man.name = '클라크'
super_man.age = 1000
super_man.speed = 1
super_man.fly = True
print(super_man)
super_man.eat()
super_man.run()
super_man.sky()