some_string = input()

letters = ""
numbers = ""
characters = ""

for sign in some_string:
    if sign.isalpha():
        letters += sign
    elif sign.isdigit():
        numbers += sign
    else:
        characters += sign

print(numbers)
print(letters)
print(characters)