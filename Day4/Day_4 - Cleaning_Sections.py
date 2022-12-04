import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    
    sections = f.read().split('\n')
    

score = 0
for pair in sections:
    elves = pair.split(',')
    elves = [x.split('-') for x in elves]
    start_1, end_1 = [int(x) for x in elves[0]]
    start_2, end_2 = [int(x) for x in elves[1]]
    
    if start_1 >= start_2 and end_1 <= end_2:
        score += 1
    elif start_2 >= start_1 and end_2 <= end_1:
        score += 1
    
print(score)


overlap_score = 0
for pair in sections:
    elves = pair.split(',')
    elves = [x.split('-') for x in elves]
    start_1, end_1 = [int(x) for x in elves[0]]
    start_2, end_2 = [int(x) for x in elves[1]]
    
    if start_1 <= end_2 and end_1 >= start_2:
        overlap_score += 1
    elif start_1 >= end_2 and end_1 <= start_2:
        overlap_score += 1
    
print(overlap_score)