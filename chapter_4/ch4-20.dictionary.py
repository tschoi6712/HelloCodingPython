"""""""""""""""""""""""
딕셔너리
"""""""""""""""""""""""

# 딕셔너리 : 문자열 기반으로 값을 저장 {키:값}
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}
print(dictionary)

# 딕셔너리 요소에 접근하기
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])

dictionary["name"] = "8D 건조 망고"     # 값을 변경
print("name:", dictionary["name"])

# 키가 존재하는지 확인하고 값에 접근하기(1)
if "존재하지 않는 키" in dictionary:
    print(dictionary["존재하지 않는 키"])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

# 키가 존재하는지 확인하고 값에 접근하기(2)
value = dictionary.get("존재하지 않는 키")
print("값:", value)
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")


# 딕셔너리에 요소 추가하기
dict_a = {}
print("요소 추가 이전:", dict_a)
dict_a["name"] = "새로운 이름"
dict_a["head"] = "새로운 정신"
dict_a["body"] = "새로운 몸"
print("요소 추가 이후:", dict_a)


# 딕셔너리 요소 제거하기
dict_b = {
    "name": "7D 건조 망고",
    "type": "당절임"
}
print("요소 제거 이전:", dict_b)
del dict_b["name"]
del dict_b["type"]
print("요소 제거 이후:", dict_b)




