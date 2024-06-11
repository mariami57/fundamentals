some_string = input()

for index in range(len(some_string)):
    if some_string[index-1] == ":":
        emoticon = some_string[index]
        print(f":{emoticon}")


