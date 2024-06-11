input_line = input().split()

some_dict = {}
for word in input_line:
    word_lower = word.lower()
    if word_lower not in some_dict:
        some_dict[word_lower] = 0
    some_dict[word_lower] += 1

for key,value in some_dict.items():
    if value % 2 != 0:
        print(key, end=" ")