import string
import itertools

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    rucksacks = f.read().split('\n')

priorities = dict(enumerate(list(string.ascii_lowercase + string.ascii_uppercase), start=1)) # paring alphabet with numbers
priorities = {v:k for (k,v) in priorities.items()} # swaping keys and values (1:a) -> (a:1)

score = 0
for compartments in rucksacks: # for each line in our list
    divider = int(len(compartments)/2) # make a divider in the middle
    for right, left in itertools.product(compartments[0: divider], compartments[divider:]): # nested loop comparing variables
        if right == left: # if variable from right side (1 compartment) is equal to var from left side - jump up the score and stop
            score += priorities[right]
            break

print(score)

badge_score = 0
for elves in range(0, len(rucksacks), 3): # loop through rucksacks with a step of 3
    for first_elf, second_elf, third_elf in itertools.product(rucksacks[elves], rucksacks[elves+1], rucksacks[elves+2]):
        if first_elf == second_elf == third_elf: # same as above but now with 3 variables
            badge_score += priorities[first_elf] # as soon as all three are equal to each other - up the score and break
            break
        
print(badge_score)