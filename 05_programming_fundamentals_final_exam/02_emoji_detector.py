import re
cool_threshold = 1

pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"

input_line = input()
for char in input_line:
    if char.isdigit():
        cool_threshold *= int(char)
print(f"Cool threshold: {cool_threshold}")
matches = re.findall(pattern, input_line)
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for match in matches:
    emoji_coolness = 0

    for letter in match[1]:
        emoji_coolness += ord(letter)
    if emoji_coolness >= cool_threshold:
        print("".join(match))





