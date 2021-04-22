class Car:
    # 클래스 : 멤버변수(인스턴스변수)+멤버함수

    # 전역변수 선언. 안에 아무것도 없음. (defalt로 초기화)
    speed = None
    color = None

    def run(self): # self = 클래스 안에 있는 함수다.
        print(self.color, '색이 달리다')
    def start(self):
        print(self.speed,'속도로 출발하다.')

    def __str__(self):
        return self.speed + ',' + self.color

if __name__ == '__main__':
    car1 = Car() # 객체 생성
    car1.color = "빨강"
    car1.speed = "100"

    print(car1.color)
    print(car1.speed)
    car1.run()
    car1.start()
    print(car1)
##########################################
    car2 = Car()
    car2.color = "파랑"
    car2.speed = "200"

    print(car2.color)
    print(car2.speed)
    car2.run()
    car2.start()
    print(car2)