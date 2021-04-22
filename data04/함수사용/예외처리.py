try:
    me_file = open("me.txt","r",encoding='utf-8') # 읽기전용, 인코딩
    print(me_file.readline())
    lines = me_file.readlines()
    print('읽어온 내용', lines)
    print(type(lines))
    me_file.close()
except IOError:
    print('파일을 읽는 중 에러발생!!!')
finally:  # finally는 무조건 실행됨.
    print('나는 예외처리를 꼭 해줌..')
print('내가 실행이 되는가......')