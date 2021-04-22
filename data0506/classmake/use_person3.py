from classmake.person_module import *

class Student(Person):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self):
        print('공부하다')


class Worker(Person):
    company = ""

    def __init__(self,name,age,company):
        self.name = name
        self.age = age
        self.company = company

    def work(self):
        print('일하다')

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' ' + self.company

if __name__ == '__main__':
    student1 = Student('홍길동',15)
    print(student1)
    student1.study()

    worker1 = Worker('김길동',30,'mega')

    # 멤버변수에 값을 주지 않았기 때문에 공백이나 0이 출력될 것.
    print(worker1)
    worker1.work()