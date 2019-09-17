"""""""""""""""""""""""""""
튜플
"""""""""""""""""""""""""""

# 튜플을 생성.
tuple_test = (10, 20, 30)

print("# 튜플의 요소 출력하기")
print("tuple_test[0]:", tuple_test[0])
print("tuple_test[1]:", tuple_test[1])
print("tuple_test[2]:", tuple_test[2])
print()

print("# 튜플은 요소를 변경 불가!!(예외가 발생합니다)")
#tuple_test[0] = 10



# 리스트와 튜플의 특이한 사용
[a, b] = [10, 20]
(c, d) = (30, 40)
e, f = 50, 60

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
print("f:", f)


# 괄호가 없는 튜플
tuple_a = 10, 20, 30, 40
print("tuple_a:", tuple_a)
print(type(tuple_a))


# 여러 개의 값을 리턴
def test():
    return 10, 20


a, b = test()

print("a:", a)
print("b:", b)

