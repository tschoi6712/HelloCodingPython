"""""""""""""""""""""""""""""""""""
객체(2)
"""""""""""""""""""""""""""""""""""


# 딕셔너리를 리턴하는 함수로 학생 성적 관리하기(2)
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92),
    create_student("김미화", 82, 86, 98, 88),
    create_student("김연화", 88, 74, 78, 92),
    create_student("박아현", 97, 92, 88, 95),
    create_student("서준서", 45, 52, 72, 78)
]

print("이름 ", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")



