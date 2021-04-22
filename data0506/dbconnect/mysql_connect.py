import pymysql

# alt + enter => 설치

# DAO역할의 모듈 : CRUD(DML)

# 정형데이터(목록이 정확히 나타나는 데이터)
# => mysql, oracle,sqlite3(관계형 데이터베이스 관리 시스템,RDBMS)
def create(id, pw, name, tel):
    # host = 주인(서버연결)
    con = pymysql.connect(host='localhost', user= 'root', password= '1234', port= 3306, db= 'shop')
    # tcp 연결
    print(con)  # 주소찍힘
    
    #cursor = db와 서버 사이의 통로에서 데이터를 처리해주는 객체
    cur = con.cursor()
    print(cur)
    
    # '',""은 괄호 안과 밖을 다르게 사용해야 함.
    sql = 'insert into member values ("' + id + '","' + pw + '","' + name + '","' + tel + '")'
    result = cur.execute(sql)
    # 인서트한 데이터의 개수
    print(result)
    
    # auto commit이 안되기때문에 자바와 다르게 commit를 따로 써줘야 함.
    con.commit()
    con.close()

def create2(data):
    # host = 주인(서버연결)
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    # tcp 연결
    print(con)  # 주소찍힘

    # cursor = db와 서버 사이의 통로에서 데이터를 처리해주는 객체
    cur = con.cursor()
    print(cur)

    # '',""은 괄호 안과 밖을 다르게 사용해야 함.
    sql = 'insert into member values (%s,%s,%s,%s)'
    result = cur.execute(sql,data)
    # 인서트한 데이터의 개수
    print('처리결과 : ',result,'개')

    # auto commit이 안되기때문에 자바와 다르게 commit를 따로 써줘야 함.
    con.commit()
    con.close()

def create3(datas):
    # host = 주인(서버연결)
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    # tcp 연결
    print(con)  # 주소찍힘

    # cursor = db와 서버 사이의 통로에서 데이터를 처리해주는 객체
    cur = con.cursor()
    print(cur)

    # '',""은 괄호 안과 밖을 다르게 사용해야 함.
    sql = 'insert into member values (%s,%s,%s,%s)'
    result = cur.executemany(sql,datas)
    # 인서트한 데이터의 개수
    print('처리결과 : ',result,'개')

    # auto commit이 안되기때문에 자바와 다르게 commit를 따로 써줘야 함.
    con.commit()
    con.close()

def read():
    # 1. mysql과 연결
    # 포트 3306 기본값이면 입력안해도 됨.
    con = pymysql.connect(host='localhost', db='shop', user='root', password='1234')
    print(con.get_host_info())

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    # 3. sql문
    sql = "select * from member where id = 'apple'"
    cur.execute(sql)
    row = cur.fetchone() # 결과를 1개만 가져올 때
    # cur.fetchall() : 조건에 맞는 목록을 전부 가져올 때 (자바에서 list)
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(row)
    print(type(row))
    print(row[0])

    # 4. con 닫기
    con.close()

def read2(id):
    # 1. mysql과 연결
    # 포트 3306 기본값이면 입력안해도 됨.
    con = pymysql.connect(host='localhost', db='shop', user='root', password='1234')
    print(con.get_host_info())

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    # 3. sql문
    sql = "select * from member where id = '" + id + "'"
    cur.execute(sql)
    row = cur.fetchone() # 결과를 1개만 가져올 때
    # cur.fetchall() : 조건에 맞는 목록을 전부 가져올 때 (자바에서 list)
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(row)
    print(type(row))

    # 4. con 닫기
    con.close()

def read3():
    # 1. mysql과 연결
    # 포트 3306 기본값이면 입력안해도 됨.
    con = pymysql.connect(host='localhost', db='shop', user='root', password='1234')
    print(con.get_host_info())

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    # 데이터를 꺼내올때 딕셔너리 형태로 가져오고싶으면 diccursor (기존형태는 tuple)
    cur = con.cursor(pymysql.cursors.DictCursor)
    print(cur)

    # 3. sql문
    sql = "select * from member"
    cur.execute(sql)
    #row = cur.fetchone() # 결과를 1개만 가져올 때
    rows = cur.fetchall()  # 조건에 맞는 목록을 전부 가져올 때 (자바에서 list)
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(rows)
    print(type(rows))  # 튜플의 튜플로 묶여서 나옴

    # for each 로 프린트
    for row in rows:
        print(row)

    print(rows[0])

    # 4. con 닫기
    con.close()

def update(id,tel):
    # 1. mysql과 연결
    # 포트 3306 기본값이면 입력안해도 됨.
    con = pymysql.connect(host = 'localhost',db='shop', user='root',password='1234')
    print(con.get_host_info())

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    # 3. sql문을 만들어서 전송함
    data = (tel,id)
    sql = "update member set tel = %s where id = %s"
    cur.execute(sql,data)  # 순서대로 tuple로 넣어줘야 한다.

    # 4. auto-commit이 안된다. 수동으로 반영시켜야 한다.
    con.commit()
    con.close()

def delete(id,pw):
    # host = 주인(서버연결)
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    # tcp 연결
    print(con)  # 주소찍힘

    # cursor = db와 서버 사이의 통로에서 데이터를 처리해주는 객체
    cur = con.cursor()
    print(cur)

    # '',""은 괄호 안과 밖을 다르게 사용해야 함.
    sql = 'delete from member where id = "' + id + '" and pw = "' + pw + '"'
    result = cur.execute(sql)
    # 인서트한 데이터의 개수
    print(result)

    # auto commit이 안되기때문에 자바와 다르게 commit를 따로 써줘야 함.
    con.commit()
    con.close()

