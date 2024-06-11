string1, string2 = input().split()
total_sum = 0

for char1, char2 in zip(string1, string2):
    total_sum += ord(char1) * ord(char2)

if len(string1) > len(string2):
    total_sum += sum(ord(char) for char in string1[len(string2):])

elif len(string2) > len(string1):
    total_sum += sum(ord(char) for char in string2[len(string1):])

print(total_sum)