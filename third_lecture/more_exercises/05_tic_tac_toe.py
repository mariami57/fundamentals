n = 3
tic_tac = []
first_player_flag = False
second_player_flag = False
for row in range(n):
    some_list = [int(x) for x in input().split()]
    tic_tac.append(some_list)



for r in  tic_tac:
    if len(set(r)) == 1:
        if 1 in set(r):
            first_player_flag = True
            break
        elif  2 in set(r):
            second_player_flag = True
            break

for column in zip(*tic_tac):
    if len(set(column)) == 1:
        if 1 in set(column):
            first_player_flag = True
            break
        elif 2 in set(column):
            second_player_flag = True
            break

if tic_tac[0][0] == tic_tac[1][1] == tic_tac[2][2] == 1 or tic_tac[0][2] == tic_tac[1][1] == tic_tac[2][0] == 1:
    first_player_flag = True

elif tic_tac[0][0] == tic_tac[1][1] == tic_tac[2][2] == 2 or tic_tac[0][2] == tic_tac[1][1] == tic_tac[2][0] == 2:
    second_player_flag = True


if first_player_flag:
    print("First player won")

elif second_player_flag:
    print("Second player won")

else:
    print("Draw!")
