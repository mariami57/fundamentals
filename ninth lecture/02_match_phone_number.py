import re

phones_string = input()
pattern = r"\+359+-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
matches = re.findall(pattern, phones_string)


print(", ".join(matches))

