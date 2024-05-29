cards = input().split()
num = int(input())


for _ in range(num):
    middle = len(cards) // 2
    left_part = cards[0:middle]
    right_part = cards[middle:]
    card_list = []
    for index in range(len(left_part)):
        card_list.append(left_part[index])
        card_list.append(right_part[index])
        cards = card_list

print(cards)