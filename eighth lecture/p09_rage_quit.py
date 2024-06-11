some_string = input()
rage_message = ""
small_message = ""
multiplier = ""
for index in range(len(some_string)):
    if not some_string[index].isdigit():
        small_message += some_string[index]
    else:
        for next_symbols in range(index, len(some_string)):
            if not some_string[next_symbols].isdigit():
                break
            multiplier += some_string[next_symbols]
        rage_message += small_message * (int(multiplier))
        small_message = ""
        multiplier = ""


rage_upper = rage_message.upper()
print(f"Unique symbols used: {len(set(rage_upper))}")
print(rage_upper)
