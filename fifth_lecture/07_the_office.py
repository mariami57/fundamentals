employees_happiness = list(map(int, input().split()))
happiness_improvement_factor = int(input())
happiness_multiplied = [happiness * happiness_improvement_factor for happiness in employees_happiness]
avg_happiness = sum(happiness_multiplied) / len(happiness_multiplied)
happier_counter = sum(person >= avg_happiness for person in happiness_multiplied)
total_count = len(happiness_multiplied)
message = "happy" if happier_counter >= total_count / 2 else "not happy"

print(f"Score: {happier_counter}/{total_count}. Employees are {message}!")

