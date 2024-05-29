number_people = input().split()
k = int(input())
result = []
skip_number = k - 1
index = 0
len_number_people = len(number_people)

while len_number_people:
    index = (skip_number + index) % len_number_people
    result.append(number_people.pop(index))
    len_number_people -= 1

print(f"[{','.join(result)}]")


