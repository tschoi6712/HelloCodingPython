"""""""""""""""""""""""
문자열의 format() 함수
"""""""""""""""""""""""

# format() 함수로 숫자를 문자열로 변환하기
format_output = "{}".format(52273)
print(type(format_output), format_output)


# format() 함수로 숫자를 문자열로 변환하기
format_output_a = "{}원".format(3000)
format_output_b = "{} {} {}".format(1, 2, 3)
format_output_c = "{} {} {}".format(1, "문자열", True)

print(format_output_a)
print(format_output_b)
print(format_output_c)

# IndexError: tuple index out of range
#"{} {}".format(1, 2, 3, 4, 5)
#"{} {} {}".format(1, 2)         # {} 기호의 개수


# 정수를 특정 칸에 출력하기
output_a = "{:d}".format(52)    # 정수
output_b = "{:5d}".format(52)   # 5칸
output_c = "{:10d}".format(52)  # 10칸
output_d = "{:05d}".format(52)  # 양수: 빈 칸을 0으로 채우기
output_e = "{:05d}".format(-52) # 음수: 빈 칸을 0으로 채우기

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈 칸을 0으로 채우기")
print(output_d)
print(output_e)


# 기호와 함께 출력하기
output_f = "{:+d}".format(52)    # 양수
output_g = "{:+d}".format(-52)   # 음수
output_h = "{: d}".format(52)    # 양수: 기호 부분 공백
output_i = "{: d}".format(-52)   # 음수: 기호 부분 공백

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)


# 조합하기
output_h = "{:+5d}".format(52)   # 기호를 뒤로 밀기: 양수
output_i = "{:+5d}".format(-52)  # 기호를 뒤로 밀기: 음수
output_j = "{:=+5d}".format(52)  # 기호를 앞으로 밀기: 양수
output_k = "{:=+5d}".format(-52) # 기호를 앞으로 밀기: 음수
output_l = "{:+05d}".format(52)  # 0으로 채우기: 양수
output_m = "{:+05d}".format(-52) # 0으로 채우기: 음수

print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)


# 부동소수점 출력형태
output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)   # 15칸 만들기
output_c = "{:+15f}".format(52.273)  # 15칸에 부호 추가하기
output_d = "{:+015f}".format(52.273) # 15칸에 부호 추가하고 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)

# 소수점 아래 자릿수 지정하기
output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)


# 의미없는 소수점 제거
output_a = 52.0
output_b = "{:g}".format(52.0)

print(output_a)
print(output_b)
