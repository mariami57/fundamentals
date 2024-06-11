import re

some_text = input()

regex = r"\s(([a-z0-9]+[a-z0-9\-\.\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
match = re.findall(regex, some_text)

for email in match:
    print(email[0])