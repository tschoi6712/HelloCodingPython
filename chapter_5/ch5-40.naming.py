"""""""""""""""""""""""""""
코드에 이름 붙이기
"""""""""""""""""""""""""""

# 주석이 붙어 있는 코드
number_input = input("숫자 입력> ")
radius = float(number_input)

print(2 * 3.14 * radius)  # 원의 둘레
print(3.14 * radius * radius)  # 원의 넓이


# 함수를 횔용한 코드
PI = 3.14


def number_input():
    output = input("숫자 입력> ")
    return float(output)


def get_circumference(radius):
    return 2 * PI * radius


def get_circle_area(radius):
    return PI * radius * radius


radius = number_input()
print(get_circumference(radius))
print(get_circle_area(radius))



