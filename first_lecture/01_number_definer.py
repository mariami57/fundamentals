number = float(input())

abs_number = abs(number)
if abs_number < 1 and abs_number != 0:
    print("small", end=" ")
elif abs_number > 1000000:
    print("large", end=" ")

if number == 0:
    print("zero")
elif number < 0:
    print("negative")
else:
    print("positive")

