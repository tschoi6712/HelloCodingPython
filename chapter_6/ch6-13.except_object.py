"""""""""""""""""""""""""""
예외 객체
"""""""""""""""""""""""""""

# 예외 객체
try:
    number_input = int(input("정수 입력> "))
    # 출력합니다.
    print("원의 반지름:", number_input)
    print("원의 둘레:", 2 * 3.14 * number_input)
    print("원의 넓이:", 3.14 * number_input * number_input)
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)



# 예외 구분하기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해주세요!")
    print("exception:", exception)
except IndexError:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)



# 모든 예외 구분하기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    # 리스트의 요소를 출력합니다.
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))

    예외.발생해주세요()
except ValueError as exception:
    print("정수를 입력해주세요!")
    print(type(exception), exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print(type(exception), exception)
except Exception as exception:
    # 이외의 예외가 발생한 경우
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(exception), exception)



# 강제로 예외 발생시키기
number = int(input("정수 입력> "))

if number > 0:
    # 양수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError
else:
    # 음수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError







