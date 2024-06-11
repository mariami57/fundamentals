def perfect_number(current_number):
    divisor_sum = 0
    for num in range(1, current_number):
        if current_number % num == 0:
            divisor_sum += num
    return divisor_sum


number = int(input())

if number == perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")