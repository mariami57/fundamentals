import math

n_students = int(input())
total_number_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_student = 0
for student in range(1, n_students+1):
    student_attendances = int(input())
    total_bonus = student_attendances / total_number_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_student = student_attendances


print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {math.ceil(max_student)} lectures.")