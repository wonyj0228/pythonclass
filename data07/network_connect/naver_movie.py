# 원격 접속하는 것
import requests
# 2차원 데이터를 만들어주는 것
import pandas as pd
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
result = requests.get(url) #result는 객체(반환)
#print(result)   # response 200 = 연결완료
#print(result.content)

# DOM트리형태의
content = BeautifulSoup(result.content,"html.parser")
#print(content)

dt_list = content.findAll("dt",{"class":"tit"})
# dt_list : resultset class의 객체,list의 상속!
# 인덱싱과 슬라이싱이 된다.
print(type(dt_list)) #resultset클래스의 객체
print(dt_list)   # tostring 내장돼있어서 다 보임 : 전체 목록 프린트
print('리스트의 개수 > ' , len(dt_list))
# print(dt_list[0])
tag = dt_list[0].find("a") # a태그만 찾기
print(tag)
print(type(tag))  # 태그라는 객체임!
print(tag.text)

print("=================================================")
dl_list=content.findAll("span",{"class":"num"})
print(dl_list)
print(type(dl_list))
print(dl_list[0].text)
print(len(dl_list))  # 예매율도 num클래스 안에 같이 있어서

print("===============================================")
for i in dl_list:
    print(i.text)

for index in range (0, len(dl_list), 2):
    print(index, ':', dl_list[index].text)

print('===============================================')
title_list = []
for i in dt_list:
    print(i.find("a").text)
    data = i.find("a").text
    title_list.append(data)
print(len(title_list))
print(title_list)

jumsu_list = []
for i in range(0,145):
    data = dl_list[i].text
    jumsu_list.append(data)
print(len(jumsu_list))
print(jumsu_list)

title_list2 = tuple(title_list)
print(title_list2)
jumsu_list2 = tuple(jumsu_list)
print(jumsu_list2)

# 여러목록의 집합체를 하나씩 꺼내서 묶어주는 것 = zip
total=list(zip(title_list2,jumsu_list2))
total_list = tuple(total)
print(total_list)

import mysql_movie.movie_crud as db
db.create(total_list)
