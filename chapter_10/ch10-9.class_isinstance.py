"""""""""""""""""""""""""""""""""""""""
클래스 - 어떤 크래스의 인스턴스인지 확인하기
"""""""""""""""""""""""""""""""""""""""


# 학생 클래스를 선언
class Student:
    def study(self):
        print("공부를 합니다.")

# 선생님 클래스를 선언
class Teacher:
    def teach(self):
        print("학생을 가르칩니다.")

# 교실 내부의 객체 리스트를 생성
classroom = [Student(), Student(), Teacher(), Student(), Student()]

# 반복을 적용해서 적절한 함수를 호출
for person in classroom:
    if isinstance(person, Student):
        person.study()
    else:
        person.teach()