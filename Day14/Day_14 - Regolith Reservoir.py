import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    rock_positions = f.read().split('\n')


no_arrow_coords = []

for line in rock_positions:
    line_coords = []
    
    for coords in  line.split(' -> '):
        pair = [int(coords.split(',')[0]), int(coords.split(',')[1])]
        line_coords.append(pair)
        
    no_arrow_coords.append(line_coords)
        

for line in no_arrow_coords:
    
    pairs_paired = 0
    line_length = len(line)
    
    while pairs_paired != (line_length - 1):
    
        for pair_index in range(line_length): # from 0 to len(line)
            
            if pair_index != line_length - 1: # untill we reached the last element
                
                start_x = line[pair_index][0]
                start_y = line[pair_index][1]
                end_x = line[pair_index + 1][0]
                end_y = line[pair_index + 1][1]
                
                
                if (start_x == end_x) and (start_y != end_y):
                    
                    sorted_coords = sorted([start_y, end_y])
                    
                    for intersect_y in range(1, abs(start_y - end_y) + 1):
                        
                        intersected_pair = [start_x, sorted_coords[0] + intersect_y]
                        
                        if intersected_pair not in line:
                            
                            line.append(intersected_pair)
                
                
                if (start_x != end_x) and (start_y == end_y):
                    
                    sorted_coords = sorted([start_x, end_x])
                    
                    for intersect_x in range(1, abs(start_x - end_x) + 1):
                        
                        intersected_pair = [sorted_coords[0] + intersect_x, start_y]
                        
                        if intersected_pair not in line:
                            
                            line.append(intersected_pair)
                            
                
                pairs_paired += 1


obstacles = []
for line in no_arrow_coords:
    for pair in line:
        if pair not in obstacles:
            obstacles.append(pair)


set_obstacles = set()
for pair in obstacles:
    
    set_obstacles.add('/'.join([str(x) for x in pair]))


row = 0
col = 500

max_depth = sorted(obstacles, key = lambda x: x[1])[-1][1]

floor = max_depth + 2

settled_grains_of_sand = 0


while '500/0' not in set_obstacles:
    
    if [col, row + 1] == [col, floor]:
        set_obstacles.add('/'.join([str(col), str(row)]))
        settled_grains_of_sand += 1
        row = 0
        col = 500
        continue
        
    
    if '/'.join([str(col), str(row + 1)]) not in set_obstacles:
        row += 1
    
    elif '/'.join([str(col - 1), str(row + 1)]) not in set_obstacles:
        row += 1
        col -= 1
    
    elif '/'.join([str(col + 1), str(row + 1)]) not in set_obstacles:
        row += 1
        col += 1
        
    else:
        set_obstacles.add('/'.join([str(col), str(row)]))
        settled_grains_of_sand += 1
        row = 0
        col = 500
        
print(settled_grains_of_sand)



# picture

picture = []
for j in range(floor):
    ryad = []
    for i in range(400, 600):
        if '/'.join([str(i), str(j)]) in set_obstacles:
            ryad.append('x')
        else:
            ryad.append('.')
    
    picture.append(ryad)
    
for line in picture:
    print(''.join(line))