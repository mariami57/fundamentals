some_string = input().split()
for string in some_string:
    if " " in string:
        string.strip()
total = 0
for string in some_string:
    numbers = int(string[1:-1])
    if string[0].isupper():
        first_result = numbers / ((ord(string[0].lower())) - 96)
    else:
        first_result = numbers * ((ord(string[0].lower())) - 96)

    if string[-1].isupper():
        second_result = first_result - ((ord(string[-1].lower())) - 96)
    else:
        second_result = first_result + ((ord(string[-1].lower())) - 96)
    total += second_result

print(f"{total:.2f}")
