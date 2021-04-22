from classmake.person_module import *

# import를 단축키(allyias..?)로 쓰는 방법
import classmake.everyday as my

# my와 person을 두개 다 상속받을 때
# 자바 = 클래스간 상속은 단일상속만 가능
# c++, 파이썬 = 클래스간 다중상속 가능
class WomanDay(Person,my.Day):

    #womanday 생성자에 입력값 넣어주기
    def __init__(self,type1,time1,location1):
        # day생성자에 넣어주기
        my.Day.__init__(self,type1,time1,location1)

    def free(self):
        print('쉬다.!')

    def __str__(self):
        return self.type1 + ' ' + str(self.time1) + ' ' + self.location1

if __name__ == '__main__':
    woman_day1 = WomanDay('진짜 놀기',20,'마포구')
    woman_day1.free()
    woman_day1.eat()
    print(woman_day1)
