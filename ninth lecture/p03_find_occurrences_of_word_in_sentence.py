import re

input_line = input()
searched_word = input()
pattern = fr"(?i)\b{searched_word}\b"
match = re.findall(pattern, input_line)

print(len(match))
