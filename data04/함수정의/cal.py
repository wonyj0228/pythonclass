# 함수의 입력값, 리턴값에 대한 타입 지정 x

def add(x,y):
    return x+y
def minus(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

# 간단히 테스트. 위치가 함수보다 위에 있다면 사용 불가. 프로그램은 위에서부터 코드를 읽음.
if __name__ == '__main__':
    print('더한 결과>> ', add(1000,200))

# 파일이 호출받는다면 위에 코드도 같이 실행됨.
# 따라서 메인안에 넣어서 이 모듈 안에서만 실행시킬 것.