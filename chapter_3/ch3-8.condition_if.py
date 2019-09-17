"""""""""""""""""""""""
if 조건문
"""""""""""""""""""""""

# 조건문
number = input("정수 입력> ")
number = int(number)

# 양수 조건
if number > 0:
    print("양수입니다")
# 음수 조건
if number < 0:
    print("음수입니다")
# 0 조건
if number == 0:
    print("0입니다")


# 날짜/시간 출력하기
import datetime
now = datetime.datetime.now()

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")


# 오전과 오후를 구분하는 프로그램
import datetime
now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시간은 {}시로 오전입니다!".format(now.hour))
if now.hour >= 12:
    print("현재 시간은 {}시로 오후입니다!".format(now.hour))


# 계절 구분(1)
import datetime
now = datetime.datetime.now()

if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))
if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))
if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))


# 짝수와 홀수 구분(1)
number = input("정수 입력> ")
number = int(number)
# 문자열로 변환
number = str(number)
# 마지막 자리 숫자를 추출
last_character = number[-1]
# 숫자로 변환하기
last_number = int(last_character)
# 짝수 확인
if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수입니다")
# 홀수 확인
if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9:
    print("홀수입니다")


# 짝수와 홀수 구분(2)
number = input("정수 입력> ")
number = int(number)

# 짝수 조건
if number % 2 == 0:
    print("짝수입니다")
# 홀수 조건
if number % 2 != 0:
    print("홀수입니다")

