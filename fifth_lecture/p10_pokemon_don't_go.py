distances = list(map(int, input().split()))
sum_elements = 0
while distances:
    index = int(input())
    target = 0
    if 0 <= index < len(distances):
        target = distances[index]
        del distances[index]
    elif 0 > index:
        index = 0
        target = distances[index]
        distances.pop(0)
        distances.insert(index, distances[len(distances) - 1])
    else:
        index = len(distances)
        distances.insert(index, distances[0])
        target = distances[index-1]
        distances.pop(index - 1)

    sum_elements += target
    for distance_index in range(len(distances)):
        if distances[distance_index] <= target:
            distances[distance_index] += target
        else:
            distances[distance_index] -= target

print(sum_elements)



