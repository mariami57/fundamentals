import re

some_text = input()

regex = r"\bwww\.[A-Za-z0-9\-]+\.[a-z\.]+"

while some_text:
    matches = re.findall(regex, some_text)
    if matches:
        print("".join(matches))
    some_text = input()

