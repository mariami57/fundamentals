import re

input_line = input()

pattern = r"\b_([A-Za-z0-9]+)\b"

match = re.findall(pattern, input_line)

print(",".join(match))