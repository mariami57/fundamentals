command = input()
employees = {}
while command != "End":
    command = command.split(" -> ")
    company_name, emp_id = command[0], command[1]
    if company_name not in employees:
        employees[company_name] = [emp_id]
    else:
        if emp_id not in employees[company_name]:
            employees[company_name].append(emp_id)

    command = input()

for company_name, emp_id in employees.items():
    print(company_name)
    for emp_id in employees[company_name]:
        print(f"-- {emp_id}")
