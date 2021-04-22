import pymysql

def create(data):
    # 1. db연결
    con = pymysql.connect(host='localhost',db='shop',user='root',password='1234')
    print('db연결 완료')

    # 2.  스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득
    cur = con.cursor()
    print('cursor획득')

    # 3. sql문
    sql = "insert into board values(%s,%s,%s,%s)"
    result = cur.execute(sql,data)
    
    # 4. commit, close
    con.commit()
    print('처리결과 ',result,'개')
    
    con.close()

def update(data):
    # 1. db연결
    con = pymysql.connect(host='localhost', db='shop', user='root', password='1234')
    print('db연결 완료')

    # 2.  스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득
    cur = con.cursor()
    print('cursor획득')

    # 3. sql문
    sql = "update board set title = %s, content = %s where id = %s"
    result = cur.execute(sql, data)

    # 4. commit, close
    con.commit()
    print('처리결과 ', result, '개')

    con.close()

def read(data):
    # 1. db연결
    con = pymysql.connect(host='localhost', db='shop', user='root', password='1234')
    print('db연결 완료')

    # 2.  스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득
    cur = con.cursor()
    print('cursor획득')

    # 3. sql문
    sql = "select * from board where id = %s"
    cur.execute(sql,data)
    row = cur.fetchone()
    print(row)

    # 4. close
    con.close()

def all():
    # 1. db연결
    con = pymysql.connect(host='localhost', db='shop', user='root', password='1234')
    print('db연결 완료')

    # 2.  스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득
    cur = con.cursor()
    print('cursor획득')

    # 3. sql문
    sql = "select * from board"
    cur.execute(sql)
    rows = cur.fetchall()
    print('db개수는 : ', len(rows))
    for row in rows:
        print(row)

    # 4. close
    con.close()