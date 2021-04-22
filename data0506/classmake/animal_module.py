# class의 역할 : 틀의 역할!
# => object : 틀을 가지고 만든 실제 대상(객체, 우리가 쓸 수 있는 부품의 형태)

class Dog:

    # 멤버변수
    color = None
    field = ''

    # 생성자 함수(객체생성시 자동호출되는 함수, 초기화를 담당)
    def __init__(self,color,field):
        # 생성자에 넣는 가장 많은 초기화처리는 멤버변수값 초기화임.
        self.color = color
        self.field = field
        print('생성자가 호출됨.')

    # 오버라이드(재정의)
    # tostring 주소말고 속성값을 보여주도록. return으로 string을 내보냄
    def __str__(self):
        return 'dog의 속성값들 > ' + str(self.color) + ', ' + self.field

    # 멤버함수
    def jump(self):
        print('강아지가 점프한다.')

    def sleep(self):
        print('강아지가 잔다.')

# 실행할 메인 생성
if __name__ == '__main__':
    dog1 = Dog('white','진돗개')  # 객체생성! 생성자 함수 실행됨.   # dog1,dog2는 참조형 변수
    dog2 = Dog('blue','요크셔테리어')  # 참조형(주소) = 데이터들이 들어있는 영역에 대한 주소.
    # 객체 생성할 때 dog1에 대한 특성을 저장하기 위해 멤버변수(color, field)가 heap영역에 복사된다.
    print(dog1)
    dog1.jump()
    print(dog2)
    dog2.sleep()


