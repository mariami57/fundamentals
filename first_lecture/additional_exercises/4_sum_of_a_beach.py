from collections import Counter
word = input()
lower_case = word.lower()
lower_list = list(lower_case)
counter_sun = lower_case.count("sun")
counter_sand = lower_case.count("sand")
counter_water = lower_case.count("water")
counter_fish = lower_case.count("fish")
print(counter_fish + counter_sand + counter_water + counter_sun)