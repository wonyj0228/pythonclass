import dbconnect.mysql_connect as db

# id = input('아이디를 입력하세요.')
# pw = input('패스워드를 입력하세요.')
# name = input('이름을 입력하세요.')
# tel = input('전화번호를 입력하세요.')

# 튜플 생성
data1 = ("data1","data1","data1","data1")  # vo역할
data2 = ("data2","data2","data2","data2")
data3 = ("data3","data3","data3","data3")
datas = (data1,data2,data3)
print('입력된 데이터들 > ', datas)
db.create3(datas)