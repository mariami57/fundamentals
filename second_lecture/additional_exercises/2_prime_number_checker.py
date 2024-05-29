num = int(input())
counter = 0

for number1 in range(1, num+1):
    for number2 in range(1, num+1):
        if number1 * number2 == num:
            if number1 != num and number2 != num:
                counter -= 1
                continue
            else:
                counter += 1
if counter == 2:
    print("True")
else:
    print("False")


