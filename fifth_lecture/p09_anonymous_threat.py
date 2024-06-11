some_string = input().split()
input_line = input().split()

while input_line[0] != "3:1":
    if input_line[0] == "merge":
        start_index, end_index = int(input_line[1]), int(input_line[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(some_string) -1:
            end_index = len(some_string) -1
        merged_elements = "".join(some_string[start_index:end_index+1])
        some_string[start_index:end_index + 1] = [merged_elements]
    elif input_line[0] == "divide":
        index = int(input_line[1])
        partitions = int(input_line[2])
        element = some_string[index]
        divided_partition = []
        partition_length = len(element) // partitions
        for current_element_index in range(partitions):
            if current_element_index != partitions - 1:
                divided_partition.append(
                    element[current_element_index * partition_length: (current_element_index + 1) * partition_length])
            else:
                divided_partition.append(element[current_element_index * partition_length:])
        some_string[index:index + 1] = divided_partition

    input_line = input().split()

print(" ".join(some_string))





