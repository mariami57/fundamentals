
# word = ""
# for char in some_sting:
#     if char.lower() not in ['a', 'o', 'u', 'e', 'i']:
#         word += char
#
# print(word)
some_sting = input()

word = [char for char in some_sting if char.lower() not in ['a', 'o', 'u', 'e', 'i']]

print("".join(word))