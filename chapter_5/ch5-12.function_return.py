"""""""""""""""""""""""""""
함수(리턴)
"""""""""""""""""""""""""""


# 리턴
def return_test():
    print("A 위치입니다.")
    return                  # 함수를 실행했던 위치로 돌아간다
    print("B 위치입니다.")


return_test()


# 자료와 함께 리턴하기
def return_test():
    return 100              # 리턴값을 가지고 함수를 실행했던 위치로 돌아간다


value = return_test()
print(value)


# 범위 안의 정수를 모두 더하는 함수
def sum_all(start, end):
    # 변수를 선언.
    output = 0
    for i in range(start, end + 1):
        output += i
    return output


print("0 to 100:", sum_all(0, 100))
print("0 to 1000:", sum_all(0, 1000))
print("50 to 100:", sum_all(50, 100))
print("500 to 1000:", sum_all(500, 1000))


# 기본매개변수와 키워드매개변수를 활용한 범위 안의 정수를 모두 더하는 함수
def sum_all(start=0, end=100, step=1):
    # 변수를 선언.
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output


print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))


