"""""""""""""""""""""""""""
예외 처리(finally)
"""""""""""""""""""""""""""

# 파일이 제대로 닫혔는지 확인하기
try:
    file = open("file.txt", "w")
    예외.발생해라()
    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# 파일이 제대로 닫혔는지 확인하기(finally)
try:
    file = open("file.txt", "w")
    예외.발생해라()
except Exception as e:
    print(e)
finally:
    file.close()

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# 파일이 제대로 닫혔는지 확인하기(try except 구문 완료후 close())
try:
    file = open("file.txt", "w")
    예외.발생해라()
except Exception as e:
    print(e)

file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)


# try 구문 내부에 return 을 사용
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")


print(test())

