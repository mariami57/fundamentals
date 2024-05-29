first_index = int(input())
second_index = int(input())
char_string = ""
for index in range(first_index, second_index+1):
    char_string += chr(index)

print(" ".join(char_string))