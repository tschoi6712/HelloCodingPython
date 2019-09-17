"""""""""""""""""""""""""""
재귀함수
"""""""""""""""""""""""""""


# 반복문으로 팩토리얼 구하기
def factorial(n):
    # 변수를 선언.
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output


print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))


# 재귀함수로 팩토리얼 구하기
def factorial(n):
    # n이 1이라면 1을 리턴
    if n == 1:
        return 1
    # n이 1이 아니라면 n * (n-1)!을 리턴
    else:
        return n * factorial(n - 1)


print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))


# 재귀함수로 구현한 피보나치 수열
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("fibonacci(1):", fibonacci(1))
print("fibonacci(2):", fibonacci(2))
print("fibonacci(3):", fibonacci(3))
print("fibonacci(4):", fibonacci(4))
print("fibonacci(5):", fibonacci(5))
print("fibonacci(6):", fibonacci(6))

# 피보나치 함수의 문제 찾기
counter = 0


def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter                              # 함수 내부에서 외부 변수를 참조
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))


# 재귀함수의 메모화
dictionary = {
    1: 1,
    2: 1
}


def fibonacci(n):
    if n in dictionary:
        # 메모 되어 있으면 메모된 값 리턴
        return dictionary[n]
    else:
        # 메모 되어 있지 않으면 값을 구함
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output


print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))



