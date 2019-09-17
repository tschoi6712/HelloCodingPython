"""""""""""""""""""""""
break 와 continue 키워드
"""""""""""""""""""""""


# break 키워드
i = 0
while True:
    # 몇 번째 반복인지 출력합니다.
    print("{}번째 반복문입니다".format(i))
    i = i + 1
    # 반복을 종료합니다.
    input_text = input("> 종료하시겠습니까?(y): ")
    if input_text in ["y", "Y"]:
        print("반복을 종료합니다.")
        break



# continue 키워드
numbers = [5, 15, 6, 20, 7, 25]
for number in numbers:
    # number 가 10보다 작으면 다음 반복으로 넘어갑니다.
    if number < 10:
        continue
    print(number)
