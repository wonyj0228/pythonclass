import pymysql

def create(data):
    # host = 주인(서버연결)
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    # tcp 연결
    print(con.get_host_info())  # 주소찍힘

    # cursor = db와 서버 사이의 통로에서 데이터를 처리해주는 객체
    cur = con.cursor()
    print(cur)

    sql = 'insert into comic(ctitle,cwriter,crate) values (%s,%s,%s)'
    result = cur.executemany(sql, data)
    # 인서트한 데이터의 개수
    print('처리결과 : ', result, '개')

    # auto commit이 안되기때문에 자바와 다르게 commit를 따로 써줘야 함.
    con.commit()
    con.close()
