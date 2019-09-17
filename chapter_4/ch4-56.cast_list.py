"""""""""""""""""""""""""""
리스트로 변환하기
"""""""""""""""""""""""""""

# list() 함수 결과
example_a = "문자열"
example_b = { "키A":"값A", "키B": "값B" }
example_c = range(10)

print("list({}) = {}".format(example_a, list(example_a)))
print("list({}) = {}".format(example_b, list(example_b)))
print("list({}) = {}".format(example_c, list(example_c)))

# 반복문과 iterable(문자열, 리스트, 딕셔너리, 범위)
print("# 문자열에 반복 적용")
for char in example_a:
    print("-", char)

print("# 딕셔너리에 반복 적용")
for key in example_b:
    print("-", key)

print("# 범위에 반복 적용")
for i in example_c:
    print("-", i)




