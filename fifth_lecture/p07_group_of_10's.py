list_of_numbers = list(map(int, input().split(", ")))
group = 10
while list_of_numbers:
    filtered_numbers = [number for number in list_of_numbers if number <= group]
    print(f"Group of {group}'s: {filtered_numbers}")
    list_of_numbers = [remaining_number for remaining_number in list_of_numbers if remaining_number not in filtered_numbers]
    group += 10
