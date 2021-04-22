def exam01(x,y):
    print('아이디가',x,'인',y,'님이 로그인되었습니다.')

def exam02(x,y):
    print('두 수의 합은',x+y)
    print('두 수의 차는',x-y)
    print('두 수의 곱은',x*y)
    print('두 수의 나눗셈은',x/y)
    print('나누고나서의 나머지는',x%y)

def exam03(x,y):
    age = y+10
    after_age = str(age)
    str1 = x + '님의 10년 후의 나이는 '+ after_age+'세입니다.'
    return str1

def exam04(x):
    if x > 10000:
        print('엄마 너무 용돈이 많아요.')
    elif x == 10000:
        print('감사합니다.')
    else:
        print('엄마 너무 용돈이 적어요.')

def exam05(x):
    if x%2 == 0:
        print('짝수입니다.')
    else:
        print('홀수입니다.')

def exam06(x):
    if x >= 1000:
        print('축하합니다. 실적을 달성하셨습니다.!')
        bonus = str(x*0.2)
        print('당신의 이번달 보너스는',bonus,'만원입니다.')
    else:
        print('실적을 달성하지 못했습니다.')

def exam07(x,y,z):
    moving = str(y+z)
    m_str = x+'미사일이 ' + moving + '로 이동되었습니다.'
    return m_str

def exam08(x,y):
    tax = y*0.1
    change = x-y
    return tax,change

def exam09():
    for _ in range(1000):
        print('*',end=' ')