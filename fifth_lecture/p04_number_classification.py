def positive_numbers(numbers):
    return ", ".join([number for number in numbers if int(number) >= 0])


def negative_numbers(numbers):
    return ", ".join([number for number in numbers if int(number) < 0])


def even_numbers(numbers):
    return ", ".join([number for number in numbers if int(number) % 2 == 0])


def odd_numbers(numbers):
    return ", ".join([number for number in numbers if int(number) % 2 != 0])


numbers_string = input(). split(", ")


print(f"Positive: {positive_numbers(numbers_string)}")
print(f"Negative: {negative_numbers(numbers_string)}")
print(f"Even: {even_numbers(numbers_string)}")
print(f"Odd: {odd_numbers(numbers_string)}")