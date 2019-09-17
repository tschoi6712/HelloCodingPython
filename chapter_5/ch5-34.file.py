"""""""""""""""""""""""""""
파일 처리
"""""""""""""""""""""""""""

# 파일 열고 닫기
file = open("basic.txt", "w")
file.write("Hello Python Programming...!")
file.close()


# with open("파일경로", "모드") as 파일객체:
with open("basic.txt", "r") as file:
    contents = file.read()
    print(contents)



# 랜덤한 100명의 키와 몸무게 만들기
import random

hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt", "w") as file:
    for i in range(100):
        # 랜덤한 값으로 변수를 생성
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))


# 반복문으로 파일 한 줄씩 읽기기
with open("info.txt", "r") as file:
    for line in file:
        # 변수를 선언합니다.
        (name, weight, height) = line.strip().split(",")
        # 데이터가 문제 없는지 확인합니다: 문제가 있으면 지나감
        if (not name) or (not weight) or (not height):
            continue
        # bmi = kg / (m*m)
        bmi = int(weight) / (int(height) * int(height)) * 10000
        result = ""
        if 25 <= bmi:
            result = "과제중"
        elif 18.5 <= bmi:
            result = "정상체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))


# 한 라인씩 파일 저장하기
lines =["안녕하세요.\n", "줄바꿈이 될까요\n", "안될까요? \n", "띄어쓰기라도 들어가주지 않을까요?"]
with open("test.txt", "w") as file:
    print(file.writelines(lines))

