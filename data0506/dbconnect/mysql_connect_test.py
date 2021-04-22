import pymysql

# alt + enter => 설치
#host = 주인(서버연결)
con = pymysql.connect(host='localhost', user= 'root', password= '1234', port= 3306, db= 'shop')
# tcp 연결
print(con)  # 주소찍힘

#cursor = db와 서버 사이의 통로에서 데이터를 처리해주는 객체
cur = con.cursor()
print(cur)

# '',""은 괄호 안과 밖을 다르게 사용해야 함.
sql = 'insert into member values ("python1","python1","python1","python1")'
result = cur.execute(sql)
# 인서트한 데이터의 개수
print(result)

# auto commit이 안되기때문에 자바와 다르게 commit를 따로 써줘야 함.
con.commit()