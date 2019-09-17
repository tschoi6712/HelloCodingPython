""""""""""""""""""""""
표준모듈
"""""""""""""""""""""""


# math 모듈
import math

print("math.sin(1):", math.sin(1))
print("math.cos(1):", math.cos(1))
print("math.tan(1):", math.tan(1))
print("math.log(2,10):", math.log(2,10))

print("math.floor(2.5):", math.floor(2.5))  # 내림
print("math.ceil(2.5):", math.ceil(2.5))    # 올림
print("짝수 round(2.5):", round(4.5))        # 반올림
print("홀수 round(3.5):", round(3.5))        # 반올림



# random 모듈
import random

print("- random():", random.random())                   # 0.0 <= x < 1.0 사이의 float 을 리턴
print("- uniform(10, 20):", random.uniform(10, 20))     # 지정한 범위 사이의 float 을 리턴
print("- randrange(10)", random.randrange(10))          # 지정한 범위의 int 를 리턴
print("- choice([1, 3, 4, 5]):", random.choice([1, 3, 4, 5])) # 리스트 내부에 있는 요소를 랜덤하게 선택
print("- shuffle([1, 2, 3, 5]):", random.shuffle([1, 2, 3, 5])) # 리스트의 요소들을 랜덤하게 섞음
print("- sample([1, 2, 4, 5], k=2):", random.sample([1, 2, 4, 5], k=2)) # 리스트의 요소 중에 k개를 뽑음


# sys 모듈
import sys

print("argv: ", sys.argv)       # 명령 매개변수
print("getwindowsversion:()", sys.getwindowsversion())
print("copyright:", sys.copyright)
print("version:", sys.version)
sys.exit()          # 프로그램을 강제로 종료


# os  모듈
import os

print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

print("폴더 만들기: ", os.mkdir("hello"))
print("폴더 제거하기: ", os.rmdir("hello"))

with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")
os.remove("new.txt")
# os.unlink("new.txt")

os.system("dir")        # 시스템 명령어 실행


# datetime 모듈
import datetime

print("# 현재 시간 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
    now.month,\
    now.day,\
    now.hour,\
    now.minute,\
    now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()


print("# datetime.timedelta 으로 시간 더하기")
after = now + datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))



# time 모듈
import time

print("지금부터 5초 동안 정지합니다!", time.sleep(5))




