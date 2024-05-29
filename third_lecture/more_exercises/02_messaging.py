index_codes = input().split()
some_string = list(input())
message = ""

for digit in index_codes:
    sum_codes = 0
    for number in str(digit):
        sum_codes += int(number)
    if sum_codes >= len(some_string):
        sum_codes -= (len(some_string))
    for i in range(0,len(some_string) + 1):
        if sum_codes == i:
            message += some_string[i]
            some_string.remove(some_string[i])

print(message)


