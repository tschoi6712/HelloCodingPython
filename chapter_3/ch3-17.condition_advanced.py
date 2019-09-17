"""""""""""""""""""""""
조건문 활용
"""""""""""""""""""""""

# 학점 평점
score = float(input("학점 입력> "))

if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현 체제의 수호자")
elif 2.8 <= score:
    print("일반인")
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score:
    print("오락문화의 선구자")
elif 1.0 <= score:
    print("불가촉천민")
elif 0.5 <= score:
    print("자벌레")
elif 0 < score:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗")


# False 값으로 변환 : None, 숫자 0과 0.0, 빈 컨테이너
print("# if 조건문에 0 넣기")
if 0:
    print("0은 True로 변환됩니다")
else:
    print("0은 False로 변환됩니다")
print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다")
else:
    print("빈 문자열은 False로 변환됩니다")


# pass 키워드 : 아무 의미없는 코드
number = input("정수 입력> ")
number = int(number)

if number > 0:
    # 양수일 때: 아직 미구현 상태입니다.
    pass
else:
    # 음수일 때: 아직 미구현 상태입니다.
    pass


# raise NotImplementedError 오류 강제 발생
number = input("정수 입력> ")
number = int(number)
# 조건문 사용
if number > 0:
    # 양수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError
else:
    # 음수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError
