input_line = input()
students = []
course_to_search = None
while True:

    if ":" not in input_line:
        course_to_search = input_line
        break

    input_line = input_line.split(":")
    student_name = input_line[0]
    student_id = input_line[1]
    course = input_line[2]
    students.append({'name': student_name, 'id': student_id, 'course': course})

    input_line = input()

for student in students:
    if course_to_search.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['id']}")
