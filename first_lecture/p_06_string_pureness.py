string_num = int(input())

for _ in range(string_num):
    current_string = input()

    if "," in current_string or "." in current_string or "_" in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")