card = input()
card_list = card.split("")
team_a_set = set()
team_b_set = set()
termination_flag = False

for player in card_list:
    if "A" in player:
        team_a_set.add(player)
        if len(team_a_set) > 4:
            termination_flag = True
            break
    elif "B" in player:
        team_b_set.add(player)
        if len(team_b_set) > 4:
            termination_flag = True
            break

remaining_a_players = 11 - len(team_a_set)
remaining_b_players = 11 - len(team_b_set)

print(f"Team A - {remaining_a_players}; Team B - {remaining_b_players}")
if termination_flag:
    print("Game was terminated")
