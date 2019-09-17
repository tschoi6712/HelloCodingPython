"""""""""""""""""""""""""""
람다 함수
"""""""""""""""""""""""""""


# 함수의 매개변수로 함수 전달하기
def call_10_times(func):
    for i in range(10):
        func() 


def print_hello():
    print("안녕하세요")


print(call_10_times(print_hello))


# map() 함수와 filter() 함수
def power(item):
    return item * item


def under_3(item):
    return item < 3


input_a = [1, 2, 3, 4, 5]

output_a = map(power, input_a)                      # 리스트 요소를 함수에 넣고 리턴값으로 새로운 리스트 구성
print("# map() 함수의 실행 결과")
print("map(power, input_a):", output_a)
print("map(power, input_a):", list(output_a))

output_b = filter(under_3, input_a)                 # 리스트 요소를 함수에 넣고 리턴값=True 인 것으로 새로운 리스트 구성
print("# filter() 함수의 실행 결과")
print("filter(under_3, output_b):", output_b)
print("filter(under_3, output_b):", list(output_b))


# lambda 매개변수 : 리턴값
power = lambda x: x * x
under_3 = lambda x: x < 3

input_c = [1, 2, 3, 4, 5]

output_c = map(power, input_c)
print("# map() 함수의 실행 결과")
print("map(power, input_c):", output_c)
print("map(power, input_c):", list(output_c))

output_d = filter(under_3, input_c)
print("# filter() 함수의 실행 결과")
print("filter(under_3, output_d):", output_d)
print("filter(under_3, output_d):", list(output_d))


# 람다 함수의 매개변수로 바로 입력한 형태
input_e = [1, 2, 3, 4, 5]

output_e = map(lambda x: x * x, input_e)
print("# map() 함수의 실행 결과")
print("map(power, input_e):", output_e)
print("map(power, input_e):", list(output_e))

output_f = filter(lambda x: x < 3, input_e)
print("# filter() 함수의 실행 결과")
print("filter(under_3, output_f):", output_f)
print("filter(under_3, output_f):", list(output_f))


