n = int(input())
for number in range(1, n+1):
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)
    if digit_sum in [5, 7, 11]:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
