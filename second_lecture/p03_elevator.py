n_people = int(input())
capacity = int(input())
course_counter = 0

while n_people > 0:
    n_people -= capacity
    course_counter += 1

print(course_counter)