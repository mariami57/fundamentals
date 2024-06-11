number_of_people = int(input())
current_state_of_the_lift = list(map(int, input().split()))


for wagon in range(len(current_state_of_the_lift)):
    max_people = min(4 - current_state_of_the_lift[wagon], number_of_people)
    current_state_of_the_lift[wagon] += max_people
    number_of_people -= max_people

if number_of_people > 0:
    print(f"There isn't enough space! {number_of_people} people in a queue!")
elif any(current_wagon < 4 for current_wagon in current_state_of_the_lift):
    print("The lift has empty spots!")

print(*current_state_of_the_lift)


