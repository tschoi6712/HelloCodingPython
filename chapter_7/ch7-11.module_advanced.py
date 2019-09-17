""""""""""""""""""""""
표준모듈(2)
"""""""""""""""""""""""

# urllib 모듈
from urllib import request

target = request.urlopen("https://google.com")
output = target.read()
print(output)

import os

# 현재 폴더의 요소를 읽어 들이고 폴더인지 파일인지 확인하기
output = os.listdir(".")  # 현재 폴더의 파일/폴더를 출력
print("os.listdir():", output)

print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):  # 현재 폴더가 파일인지 폴더인지를 확인
        print("폴더:", path)
    else:
        print("파일:", path)


def read_folder(path):
    # 폴더의 요소 읽어 들이기
    output = os.listdir(path)
    # 폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(item):
            # 폴더라면 계속 읽어 들이기
            read_folder(item)
        else:
            # 파일이라면 출력하기
            print("파일:", item)


print(read_folder("."))


# 문자열을 십진수와 이진수 코드로 변환하기
input_a = list("Python")
print("기본 문자열:", input_a)

output_10 = []
for char in input_a:
    output_10.append(ord(char))
print("10진수:", output_10)

output_2 = []
for char in input_a:
    output_2.append(bin(ord(char)))
print("2진수:", output_2)



# 인터넷의 이미지 저장하기
from urllib import request

target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

file = open("output.png", "wb")   # [바이너리 쓰기] 모드
file.write(output)
