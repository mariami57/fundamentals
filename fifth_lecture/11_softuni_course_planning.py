course_schedule = input().split(", ")
command = input()

while command != "course start":
    command = command.split(":")
    action = command[0]
    name = command[1]

    if action == "Add":
        if name not in course_schedule:
            course_schedule.append(name)
    elif action == "Insert":
        index = int(command[2])
        if name not in course_schedule:
            course_schedule.insert(index, name)
    elif action == "Remove":
        if name in course_schedule:
            course_schedule.remove(name)
        remove_exercise = f"{name}-Exercise"
        if remove_exercise in course_schedule:
            course_schedule.remove(remove_exercise)
    elif action == "Swap":
        name_two = (command[2])
        exercise_index = course_schedule.index(name) + 1
        if name in course_schedule and name_two in course_schedule:
            name_index = course_schedule.index(name)
            name_two_index = course_schedule.index(name_two)
            course_schedule[name_index], course_schedule[name_two_index] = course_schedule[name_two_index], course_schedule[name_index]
            exercise1 = f"{name}-Exercise"
            exercise2 = f"{name_two}-Exercise"
            if exercise1 in course_schedule:
                course_schedule.remove(exercise1)
                course_schedule.insert(exercise_index, exercise1)
            if exercise2 in course_schedule:
                exercise2_index = course_schedule.index(name_two) + 1
                course_schedule.remove(exercise2)
                course_schedule.insert(exercise2_index, exercise2)
    elif action == "Exercise":

        if name in course_schedule and course_schedule[next_index] != f"{name}-Exercise":
            next_index = course_schedule.index(name) + 1
            course_schedule.insert(next_index, f"{name}-Exercise")
        elif name not in course_schedule:
            course_schedule.append(name)
            next_index = course_schedule.index(name) + 1
            course_schedule.insert(next_index, f"{name}-Exercise")
    command = input()

for i in range(1,len(course_schedule)+1):
    print(f"{i}.{course_schedule[i-1]}")