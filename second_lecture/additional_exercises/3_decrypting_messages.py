key = int(input())

number_of_lines = int(input())

for character in range(number_of_lines):
    current_char = input()
    char_place = ord(current_char)
    decoded_place = char_place + key
    decoded_char = chr(decoded_place)
    print(decoded_char, end="")