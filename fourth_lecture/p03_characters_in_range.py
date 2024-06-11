def some_chars(first_char, second_char):
    some_list = []
    for char_as_digit in range(ord(first_char)+1, ord(second_char)):
        some_list.append(chr(char_as_digit))
    return some_list


first_character = input()
second_character = input()

print(" ".join(some_chars(first_character,second_character)))