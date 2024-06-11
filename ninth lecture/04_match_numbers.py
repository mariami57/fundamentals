import re

some_string = input()
regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

match = re.finditer(regex, some_string)

for number in match:
    print(number.group(), end=" ")