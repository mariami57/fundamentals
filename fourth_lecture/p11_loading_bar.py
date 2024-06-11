def loading_bar(number):
    result = int(number / 10)
    to_print_pt_1 = result * "%"
    to_print_pt_2 = (10 - result) * "."
    if result != 10:
        return f"{number}% [{to_print_pt_1}{to_print_pt_2}]\nStill loading..."
    else:
        return f"100% Complete!\n[%%%%%%%%%%]"



n = int(input())
print(loading_bar(n))