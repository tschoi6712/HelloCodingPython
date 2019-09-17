"""""""""""""""""""""""""""""""""""""""""""""
리스트,문자열,범위,딕셔너리와 함께 사용하는 함수
"""""""""""""""""""""""""""""""""""""""""""""

# reversed() 함수로 리스트 뒤집기
list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("reversed([1, 2, 3, 4, 5]):", list_reversed)
print("list(reversed([1, 2, 3, 4, 5])):", list(list_reversed))
for i in reversed(list_a):
    print("-", i)

# enumerate() 함수와 반복문
example_list = ["요소A", "요소B", "요소C"]

i = 0                                                           # 인덱스와 요소 조합(1)
for item in example_list:
    print("{}번째 요소는 {}입니다.".format(i, item))
    i += 1

for i in range(len(example_list)):                              # 인덱스와 요소 조합(2)
    print("{}번째 요소는 {}입니다.".format(i, example_list[i]))

print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))

print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))

print("# 반복문과 enumerate() 함수 조합하기")                       # 인덱스와 요소 조합(3)
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))


# 딕셔너리의 items() 함수와 반복문
example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}
print("items():", example_dictionary.items())

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))


# 반복문을 사용한 리스트 생성
array = []
for i in range(0, 20, 2):
    array.append(i * i)
print(array)

# 리스트 내포(array comprehension)
array = [i * i for i in range(0, 20, 2)]
print(array)

# 조건을 활용한 리스트 내포
arr = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in arr if fruit != "초콜릿"]
print(output)

# 리스트 냅부의 최소값과 최대값 구하기
list_m = [52, 273, 103, 32, 57]
min_value = min(list_m)
max_value = max(list_m)
print("최소값:", min_value)
print("최대값:", max_value)

