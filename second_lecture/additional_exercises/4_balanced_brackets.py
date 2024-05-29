n = int(input())
brackets_string = ""
for _ in range(n):
    some_string = input()
    if some_string == "(" or some_string == ")":
        brackets_string += some_string

couples = []
split_step = 2
for i in range(0, len(brackets_string),split_step):
    couples.append(brackets_string[i:i+split_step])
counter_couples = 0
for item in couples:
    if item == "()":
        counter_couples += 1

if counter_couples == len(couples):
    print("BALANCED")
else:
    print("UNBALANCED")
