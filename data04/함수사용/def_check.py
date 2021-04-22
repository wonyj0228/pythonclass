from 함수정의.def_practice import *

# 문제1
print('=============1번==============')
id = input('아이디를 입력하세요 :')
name = input('이름을 입력하세요 :')
exam01(id,name)

# 문제2
print('=============2번==============')
num1 = int(input('숫자1 :'))
num2 = int(input('숫자2 :'))
exam02(num1,num2)

# 문제3
print('=============3번==============')
name2 = input('이름을 입력하세요 :')
age = int(input('나이를 입력하세요 :'))
print(exam03(name2,age))

# 문제4
print('=============4번==============')
money = int(input('엄마 용돈주세요!!! :'))
exam04(money)

# 문제5
print('=============5번==============')
num3 = int(input('숫자를 입력해보세요. 짝수 홀수를 판별해드립니다 >>'))
exam05(num3)

# 문제6
print('=============6번==============')
profit = int(input('실적을 입력하세요 >>'))
exam06(profit)

# 문제7
print('=============7번==============')
m_name = input('미사일 이름 :')
m_start = int(input('미사일의 시작값 :'))
m_move = float(input('미사일이 움직일 값 :'))
print("-----------------------")
print(exam07(m_name,m_start,m_move))

# 문제8
print('=============8번==============')
r_money = int(input('받은 돈 :'))
r_total = int(input('상품의 총액 :'))
tax, change = exam08(r_money,r_total)
print('부가세 :',tax)
print('잔돈 :',change)

# 문제9
print('=============9번==============')
exam09()