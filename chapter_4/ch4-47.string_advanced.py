"""""""""""""""""""""""""""
여러 줄 문자열
"""""""""""""""""""""""""""


number = int(input("정수 입력> "))

# if 조건문과 여러 줄 문자열(1)
if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는 짝수입니다.""".format(number, number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는 홀수입니다.""".format(number, number))

# if 조건문과 여러 줄 문자열(2)
if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.
{}는 짝수입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.
{}는 홀수입니다.""".format(number, number))

# if 조건문과 여러 줄 문자열(2)
if number % 2 == 0:
    print("입력한 문자열은 {}입니다.\n{}는 짝수입니다.".format(number, number))
else:
    print("입력한 문자열은 {}입니다.\n{}는 홀수입니다.".format(number, number))

# if 조건문과 여러 줄 문자열(3)
if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는 짝수입니다."
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는 홀수입니다."
    ).format(number, number))

# 문자열의 join() 함수
if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는 짝수입니다."
    ]).format(number, number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는 홀수입니다."
    ]).format(number, number))


# textwrap 모듈의 dedent 함수
import textwrap
number = int(input("정수 입력> "))
if number % 2 == 0:
    print(textwrap.dedent("""\
        입력한 문자열은 {}입니다.
        {}는 짝수입니다.""").format(number, number))
else:
    print(textwrap.dedent("""\
        입력한 문자열은 {}입니다.
        {}는 홀수입니다.""").format(number, number))


# 괄호로 문자열 연결하기
test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성된답니다."
)
print("test:", test)
print("type(test):", type(test))




