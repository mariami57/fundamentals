def is_palindrome(the_string: str) -> bool:
    return the_string == the_string[::-1]


some_string = input().split(", ")
for number in some_string:
    print(is_palindrome(number))

