names_string = input().split(", ")
names_sorted = sorted(names_string, key=lambda x: (-len(x),x))

print(names_sorted)