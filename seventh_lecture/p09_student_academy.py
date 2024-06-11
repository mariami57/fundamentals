n = int(input())
dict_grades = {}

for _ in range(n):
    student_name = input()
    grade = float(input())
    if student_name not in dict_grades:
        dict_grades[student_name] = [grade]
    else:
        dict_grades[student_name] += [grade]

for name, grade in dict_grades.items():
    if sum(grade) / len(grade) >= 4.5:
        print(f"{name} -> {sum(grade) / len(grade):.2f}")