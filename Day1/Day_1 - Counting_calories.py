import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    elves = f.read().split('\n\n')

elves_sep = []

for elf in elves:
    elf = elf.split('\n')
    elves_sep.append(elf)


elves_with_calories = []

for calorie_bag in elves_sep:
    calory_count = 0
    for calories in calorie_bag:
        if len(calories) != 0:
            calory_count += int(calories)
    elves_with_calories.append(calory_count)

elves_with_calories.sort(reverse=True)  

print(sum(elves_with_calories[0:3]))