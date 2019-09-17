"""""""""""""""""""""""
while 반복문
"""""""""""""""""""""""

# for i in range(10)
i = 0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i += 1


# 해당하는 값 모두 제거하기
ls = [1, 2, 1, 2, 5, 8, 9]
value = 2
# list 내부에 value 가 있다면 반복
while value in ls:
    ls.remove(value)
print(ls)


# 시간을 기반으로 반복하기
import time
unix_time = time.time()             # UNIX time : 1970년 1월 1일 0시 0초 기준으로 몇 초
# 5초 동안 반복
output = 0
target_tick = unix_time + 5
while unix_time < target_tick:
    output += 1
print("5초 동안 {}번 반복했습니다.".format(output))





