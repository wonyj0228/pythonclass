import dbconnect.mysql_connect as db

id = input('아이디를 입력하세요.')
pw = input('패스워드를 입력하세요.')

db.delete(id,pw)