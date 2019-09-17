"""""""""""""""""""""""
문자열의 추가적 기능 
"""""""""""""""""""""""

# 대소문자 바꾸기: upper() 함수와 lower() 함수
str_a = "Hello Python Programming...!"
str_upper = str_a.upper()
str_lower = str_a.lower()

print("str.upper():", str_upper)
print("str.lower():", str_lower)

# 비파괴적 함수(원본을 변화시키지 않는 함수)
str_a.upper()
print(str_a)
str_a.lower()
print(str_a)


# 문자열 공백[띄어쓰기,탭,줄바꿈] 제거하기: strip()
input_a = """
  안녕하세요
문자열의 함수를 알아봅니다
"""

print("# 공백 제거 이전")
print(input_a)
print()

print("# 공백 제거 이후")
print(input_a.strip())   # 양 옆
print(input_a.lstrip())  # 왼쪽
print(input_a.rstrip())  # 오른쪽


# 문자열 구성 파악하기 : IS() - Boolean
print('"TrainA10".isalnum():', "TrainA10".isalnum())
print('"10".isdigit():', "10".isdigit())
print('"Train".isalpha():', "Train".isalpha())


# 문자열 위치 찾기 - find() 함수와 rfind() 함수
output_a = "안녕안녕하세요".find("안녕")
output_b = "안녕안녕하세요".rfind("안녕")

print("find():", output_a)
print("rfind():", output_b)


# 문자열과 in 연산자
print('"안녕" in "안녕하세요" =', "안녕" in "안녕하세요")


# 문자열 자르기 - split(자를 문자)
output = "10 20 30 40 50".split(" ")
print(output)










