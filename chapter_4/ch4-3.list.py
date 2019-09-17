"""""""""""""""""""""""
리스트
"""""""""""""""""""""""

# 리스트 선언하기
array = [273, 32, 103, "문자열", True, False]
print(array)

# 리스트 요소에 접근하기
print(array[0])
print(array[1])
print(array[2])
print(array[1:3])
print(array[-1])
print(array[-2])
print(array[-3])
#print(array[6])     #IndexError

# 리스트 요소를 변경하기
array[0] = "변경"
print(array)

# 리스트 뒤에 요소 추가하기
array.append(4)
print(array)

# 리스트 중간에 요소 추가하기
array.insert(0, 10)
print(array)

# 리스트 뒤에 여러 요소 추가하기
array.extend([4, 5, "ok"])
print(array)

# 리스트에 값이 있는지 없는지 확인하기
print("array:", array)
print("273 in array:", 273 in array)
print("99 not in array:", 99 not in array)

# 리스트 요소 제거하기
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

del list[1]                     # 특정 위치 제거
print("del list[1]:", list)
del list[5:7]                   # 여러 요소 제거
print("del list[5:7]:", list)

list.remove(8)                  # 값으로 제거
print("list.remove(8):", list)

list.pop(2)                     # 특정 위치 제거
print("list.pop(2):", list)

list.pop()                      # 마지막 위치 제거
print("list.pop():", list)

list.clear()                    # 전체 요소 제거
print("list.clear():", list)


# 리스트 연산자
list_a = [1, 2, 3]
list_b = [4, 5, 6]
# 리스트 결합 '+'
print("list_a + list_b =", list_a + list_b)
# 리스트 반복 '*'
print("list_a * 3 =", list_a * 3)
# 길이 구하기
print("len(list_a) = ", len(list_a))











