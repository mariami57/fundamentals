import re

input_line = input()

while input_line:
    regex = r"\d+"
    match = re.findall(regex, input_line)
    if match:
        print(" ".join(match), end=" ")
    input_line = input()

