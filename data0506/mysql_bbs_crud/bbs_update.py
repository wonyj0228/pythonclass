import dbconnect.mysql_bbs.bbs_dao as db

id = input('아이디를 입력하세요 :')
title = input('수정할 제목을 입력하세요 :')
content = input('수정할 내용을 입력하세요 :')

# dao에서 사용할 순서대로 data에 넣어주기
data = (title,content,id)
db.update(data)