import re

some_string = input()
matched_names = []
regex_pattern = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
matches = re.findall(regex_pattern, some_string)

print(" ".join(matches))