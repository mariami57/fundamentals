n_rooms = int(input())
diff_total = 0
flag = False
for room in range(1, n_rooms + 1):
    chairs, visitors = input().split()
    diff = len(chairs) - int(visitors)
    diff_total += diff
    if int(visitors) > len(chairs):
        print(f"{abs(diff)} more chairs needed in room {room}")


if diff_total >= 0:
    print(f"Game On, {abs(diff_total)} free chairs left")
