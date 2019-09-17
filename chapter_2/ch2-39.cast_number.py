"""""""""""""""""""""""
문자열을 숫자로 바꾸기
"""""""""""""""""""""""

# 문자열을 숫자로 변환
output_a = int("52")
output_b = float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)

# input()함수와 float()함수
input_a = float(input("첫 번째 숫자> "))
input_b = float(input("두 번째 숫자> "))

print("덧셈 결과:", input_a + input_b)
print("뺄셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b)

# 자료형 변환시 ValueError 예외
int("안녕하세요")    # 숫자가 아닌 것을 숫자로 변환하려고 할 때
float("안녕하세요")
int("52.273")      # 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환하려고 할 때