"""""""""""""""""""""""""""
함수(매개변수)
"""""""""""""""""""""""""""


# 일반매개변수
def print_n_times(value, n):
    for i in range(n):
        print(value)


print(print_n_times("안녕하세요", 10))


# 가변매개변수(매개변수 맨 뒤) 함수
def print_n_times(n, *values):
    # n번 반복합니다.
    for i in range(n):
        # values 는 리스트처럼 활용합니다.
        for value in values:
            print(value)


print(print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍"))


# 기본매개변수(매개변수=값)
def print_n_times(value, n=2):
    # n번 반복합니다.
    for i in range(n):
        print(value)


print(print_n_times("안녕하세요"))


# 가변매개변수>기본매개변수
def print_n_times(*values, n=2):
    # n번 반복합니다.
    for i in range(n):
        # values 는 리스트처럼 활용합니다.
        for value in values:
            print(value)


print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", 3)


# 키워드 매개변수
def print_n_times(*values, n=2):
    # n번 반복합니다.
    for i in range(n):
        # values 는 리스트처럼 활용합니다.
        for value in values:
            print(value)


print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)


# 키워드매개변수>기본매개변수
def test(a, b=10, c=100):
    print(a + b + c)


print(test(10, 20, 30))
print(test(10, c=200))





