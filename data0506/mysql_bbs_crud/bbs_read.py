import dbconnect.mysql_bbs.bbs_dao as db

id = input('검색할 아이디를 입력하세요 :')

# dao에서 사용할 순서대로 data에 넣어주기
data = (id)
db.read(data)