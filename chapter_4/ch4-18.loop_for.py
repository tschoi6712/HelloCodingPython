"""""""""""""""""""""""
for 반복문
"""""""""""""""""""""""

# 반복문과 리스트
array = [273, 32, 103, 57, 52]
for element in array:
    if element > 100:
        # 출력합니다.
        print(element)

# 반복문과 문자열
for character in "안녕하세요":
    print("-", character)


# 반복문과 딕셔너리
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}
for key in dictionary:
    # 출력합니다.
    print(key, ":", dictionary[key])


# 반복문과 범위
for i in range(10):
    print(str(i) + "번째 반복입니다.")

print(range(5), list(range(5)))                 # 범위 선언[1] - range(<숫자>)
for i in range(5):
    print(str(i) + " = 반복 변수")

print(range(5, 10), list(range(5, 10)))         # 범위 선언[2] - range(<숫자>, <숫자>)
for i in range(5, 10):
    print(str(i) + " = 반복 변수")

print(range(0, 10, 2), list(range(0, 10, 2)))   # 범위 선언[3] - range(<숫자>, <숫자>, <증분>)
for i in range(0, 10, 3):
    print(str(i) + " = 반복 변수")


# 반복문과 리스트, 범위
array = [273, 32, 103, 57, 52]
for i in range(len(array)):
    # 출력합니다.
    print("{}번째 반복: {}".format(i, array[i]))


# 역반복문
for i in reversed(range(10)):
    # 출력합니다.
    print("{}번째 반복".format(i))

