command = input()
courses = {}
while command != "end":
    course_name, student = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = [student]
    else:
        courses[course_name].append(student)

    command = input()
for key, values in courses.items():
    print(f"{key}: {len(values)}")
    for value in courses[key]:
        print(f"-- {value}")