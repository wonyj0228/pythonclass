# 원격 접속
import requests
# 크롤링을 데이터를 분석해줄 도구
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekdayList.nhn?week=fri"
result = requests.get(url)
print(result) # 연결확인용

# 돔트리 형태로 content 가져오기. html형태로 가져오기
content = BeautifulSoup(result.content,"html.parser")
# print(content)

#############웹툰제목#############
dl_list = content.findAll("dl")
# print(dl_list)

title_list = []
for i in range(3,len(dl_list)):
    data = dl_list[i].find("a").text
    title_list.append(data)
print(title_list)
print(len(title_list))

#############웹툰작가#############
dd_list = content.findAll("dd",{"class":"desc"})
# print(dd_list)

writer_list = []
for i in range(3,len(dd_list)):
    data = dd_list[i].find("a").text
    writer_list.append(data)
print(writer_list)
print(len(writer_list))

#############웹툰평점#############
span_list = content.findAll("strong")
rate_list = []
for i in range(6,61):
    data = span_list[i].text
    rate_list.append(data)
print(rate_list)
print(len(rate_list))

# tuple로 각 리스트 바꿔주기
title_list2 = tuple(title_list)
writer_list2 = tuple(writer_list)
rate_list2 = tuple(rate_list)

# 각 리스트 zip해주기
total = list(zip(title_list2,writer_list2,rate_list2))
total_list = tuple(total)
print(total_list)

# db연동
import mysql_comic.comic_dao as db
db.create(total_list)
