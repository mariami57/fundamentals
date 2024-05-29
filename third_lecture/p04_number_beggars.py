some_string = input().split(", ")
n_beggars = int(input())
beggar_list = []
index = 0
for beggar in range(1,n_beggars+1):
    beggar_sum = 0

    for current_index in range(index,len(some_string), n_beggars):
        beggar_sum += int(some_string[current_index])
    beggar_list.append(beggar_sum)
    index += 1

print(beggar_list)

