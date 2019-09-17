"""""""""""""""""""""""""""""""""""
클래스 - 예외 클래스 만들기
"""""""""""""""""""""""""""""""""""


# 사용자정의 예외 클래스 만들기
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)


raise CustomException


# 자식 클래스로써 부모의 함수 재정의(오버라이드) 하기

