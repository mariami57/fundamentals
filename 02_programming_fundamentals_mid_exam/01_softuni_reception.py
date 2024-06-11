employee_one_efficiency = int(input())
employee_two_efficiency = int(input())
employee_three_efficiency = int(input())
total_employee_efficiency = employee_one_efficiency + employee_two_efficiency + employee_three_efficiency
n_students = int(input())
hours = 0
while True:
    if n_students == 0:
        break
    if n_students < total_employee_efficiency:
        possible_students = min(n_students, total_employee_efficiency)
        n_students -= possible_students
    else:
        n_students -= total_employee_efficiency

    hours += 1
    if hours % 4 == 0:
        hours += 1
        continue
print(f"Time needed: {hours}h.")

