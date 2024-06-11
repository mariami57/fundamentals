def factorial(num1, num2):
    total_factorial_first = 1
    total_factorial_second = 1
    for number in range(1, num1+1):
        total_factorial_first *= number
    for another_number in range(1, num2+1):
        total_factorial_second *= another_number
    return total_factorial_first / total_factorial_second


first_num = int(input())
second_num = int(input())
print(f"{factorial(first_num,second_num):.2f}")