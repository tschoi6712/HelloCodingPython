"""""""""""""""""""""""""""""""""""
클래스 기본
"""""""""""""""""""""""""""""""""""


# 클래스 선언 : class 클래스이름:
# 클래스를 기반으로 인스턴스 생성하기 : 인스턴스(변수) 이름 = 클래스 이름()
# 인스턴스의 속성에 접근 : 인스턴스[인덱스].생성자의 매개변수
# 인스턴스 확인하기 : isinstance(인스턴스, 클래스)
# 매서드 : 클래스가 가지고 있는 함수

# 생성자와 소멸자
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))

    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))


test = Test("A")
test = Test("B")
test = Test("C")
