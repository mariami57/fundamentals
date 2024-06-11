n = int(input())

some_dict = {}
for _ in range(n):
    word = input()
    synonym = input()

    if word in some_dict:
        some_dict[word].append(synonym)
    else:
        some_dict[word] = [synonym]

for word, synonym_list in some_dict.items():
    synonym_string = ', '.join(synonym_list)
    print(f'{word} - {synonym_string}')

