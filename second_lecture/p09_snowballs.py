import sys

number_of_snowballs = int(input())
max_value = -sys.maxsize
max_weight = 0
max_time = 0
max_quality = 0

for _ in range(1,number_of_snowballs+1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    current_ball_value = int((weight/time_needed) ** quality)
    if current_ball_value > max_value:
        max_value = current_ball_value
        max_weight = weight
        max_time = time_needed
        max_quality = quality

print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")