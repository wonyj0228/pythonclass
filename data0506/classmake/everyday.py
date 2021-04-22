# 클래스 생성
class Day:
    # 멤버 변수
    # 실제값 변수 : 인스턴스 변수(동적변수)  <-> 스태틱 변수(정적변수)
    # RDB ->  인스턴스 <-> 스키마
    type1 = ""
    time1 = 0
    location1 = ""
    count = 0

    # 생성자 메서드
    def __init__(self, type1, time1, location1):
        self.type1 = type1
        self.time1 = str(time1)
        self.location1 = location1
        print('객체 생성완료')
        # 스태틱 변수 인식
        # 스태틱 변수는 생성자에 넣어주지 않음
        Day.count += 1
        print(str(Day.count) + '개 객체가 생성됨.')

    # 멤버 메서드
    def study(self):
        return self.type1 + '를 ' + self.time1 + '시간 하다.'

    def where(self):
        return self.location1 + '에서 ' + self.type1 + '를 하다.'

    # tostring 오버라이드
    def __str__(self):
        return 'day의 속성값들>> ' + self.type1 + ', ' + self.time1 + ', ' + self.location1


if __name__ == '__main__':
    day1 = Day('파이썬공부', 10, '강남')
    print(day1)
    print(day1.study())
    print(day1.where())
    print("===================")

    day2 = Day('자바공부', 11, '신촌')
    print(day2)
    print(day2.study())
    print(day2.where())
    print("===================")

    day3 = Day('db공부', 12, '종로')
    print(day3)
    print(day3.study())
    print(day3.where())
    print("===================")
