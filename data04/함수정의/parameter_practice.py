# 기존기능과 똑같은 이름의 함수는 만들지 않음.

def list_p(x):
    for i in range(len(x)):
        print(i+1,':',x[i])
def set_p(x):
    for i in x:
        print(i)
def dic_p(x):
    for key in x:
        print(key,':',x[key])
def tuple_p(x):
    for i in x:
        print(i)

