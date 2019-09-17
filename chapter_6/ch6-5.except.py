"""""""""""""""""""""""""""
예외처리
"""""""""""""""""""""""""""

# 조건문으로 예외 처리하기
user_input = input("정수 입력> ")

if user_input.isdigit():                # 사용자 입력이 숫자로만 구성되어 있는지 확인
    number_input = int(user_input)      # 숫자로 변환

    print("원의 반지름:", number_input)
    print("원의 둘레:", 2 * 3.14 * number_input)
    print("원의 넓이:", 3.14 * number_input * number_input)
else:
    print("정수를 입력해 주세요")



# try ~ except ~ 구문으로 예외 처리
try:
    number_input = int(input("정수 입력> "))
    # 출력합니다.
    print("원의 반지름:", number_input)
    print("원의 둘레:", 2 * 3.14 * number_input)
    print("원의 넓이:", 3.14 * number_input * number_input)
except:
    print("무언가 잘못되었습니다.")



# try except else 구문으로 예외를 처리
try:
    number_input = int(input("정수 입력> "))
except:
    print("정수를 입력해 주세요!")
else:
    print("원의 반지름:", number_input)
    print("원의 둘레:", 2 * 3.14 * number_input)
    print("원의 넓이:", 3.14 * number_input * number_input)



# try except else finally 구문으로 예외를 처리
try:
    number_input = int(input("정수 입력> "))
    print("원의 반지름:", number_input)
    print("원의 둘레:", 2 * 3.14 * number_input)
    print("원의 넓이:", 3.14 * number_input * number_input)
except:
    print("정수를 입력해 주세요!")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")



# 숫자로 변환되는 것들만 리스트에 넣기
list_input = ["52", "273",  "스파이", "103"]
list_number = []
for item in list_input:
    # 숫자로 변환해서 리스트에 추가합니다.
    try:
        float(item)
        list_number.append(item)
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_input))
print("{}입니다.".format(list_number))





