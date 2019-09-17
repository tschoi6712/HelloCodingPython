"""""""""""""""""""""""""""
파괴적 함수와 비파괴적 함수
"""""""""""""""""""""""""""

# 문자열의 비파괴적 함수
string = "Hello Programming"

output = string.upper()
print("string.upper():", output)
output = string.lower()
print("string.lower():", output)
output = string.split(" ")
print("string.split():", output)



# 리스트의 파괴적 함수
list = [1, 2, 3, 4]

list.append(1)
print("list.append(1)", list)
list.remove(2)
print("list.remove(2)", list)
list.pop()
print("list.pop():", list)


# 문자열의 함수
str_a = "Hello Programming"
output = str_a.upper()
print("# 문자열의 함수 확인")
print("str_a:", str_a)
print("str_a.upper()의 결과:", output)

# 리스트의 함수
list_a = [1, 2, 3, 4]
output = list_a.append(1)
print("# 리스트의 함수 확인")
print("list_a:", list_a)
print("list_a.append()의 결과:", output)


