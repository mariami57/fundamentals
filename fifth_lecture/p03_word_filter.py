some_string = input().split()

some_list = [word for word in some_string if len(word) % 2 == 0]

print("\n".join(some_list))