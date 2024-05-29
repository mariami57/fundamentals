time_racers = input().split()
time_racers = list(map(int, time_racers))

middle = len(time_racers)//2
left_racer = time_racers[0:middle]
right_racer = time_racers[middle+1::][::-1]

winner = ""
winner_time = 0

left_racer_total_time = 0
right_racer_total_time = 0
for num in left_racer:
    if num == 0:
        left_racer_total_time *= 0.8
    left_racer_total_time += num

for num in right_racer:
    if num == 0:
        right_racer_total_time *= 0.8
    right_racer_total_time += num

if left_racer_total_time < right_racer_total_time:
    winner = "left"
    winner_time = left_racer_total_time
elif left_racer_total_time > right_racer_total_time:
    winner = "right"
    winner_time = right_racer_total_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")

