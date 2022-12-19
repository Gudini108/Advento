import os
import sys

with open(os.path.join(sys. path[0], "input.txt"), "r") as f:
    magma_droplets = f.read().split('\n')
    
    
magma_set = set()
for line in magma_droplets:
    magma_set.add('/'.join(str(x) for x in line.split(',')))
    
magma_coords = []
for line in magma_droplets:
    magma_coords.append([int(x) for x in line.split(',')])
    
    
def lookaround(position, cords=False):
    x, y, z = position[0], position[1], position[2]
    
    x_pos = '/'.join(str(i) for i in [x+1, y, z])
    x_neg = '/'.join(str(i) for i in [x-1, y, z])
     
    y_pos = '/'.join(str(i) for i in [x, y+1, z])
    y_neg = '/'.join(str(i) for i in [x, y-1, z])
    
    z_pos = '/'.join(str(i) for i in [x, y, z+1])
    z_neg = '/'.join(str(i) for i in [x, y, z-1])
    
    if cords == False:
        return (x_pos, x_neg, y_pos, y_neg, z_pos, z_neg)
    
    else:
        left = [x-1, y, z]
        right = [x+1, y, z]
        forward = [x, y+1, z]
        backwards = [x, y-1, z]
        up = [x, y, z+1]
        down = [x, y, z-1]
        
        return (left, right, forward, backwards, up, down)
        


sidecounter = 0
for cube in magma_coords: # [x, y, z]
    position = [cube[0], cube[1], cube[2]]
    
    for pos in lookaround(position):
        if pos not in magma_set:
            sidecounter += 1


print(sidecounter)


max_x = max(i[0] for i in magma_coords)
min_x = min(i[0] for i in magma_coords)

max_y = max(i[1] for i in magma_coords)
min_y = min(i[1] for i in magma_coords)

max_z = max(i[2] for i in magma_coords)
min_z = min(i[2] for i in magma_coords)


# waterwind = set()
# waterwind_list = []
# for i in range(min_x-1, min_x+1):
#     for j in range(min_y-1, min_y+1):
#         for k in range(min_z-1, min_z+1):
#             waterwind.add('/'.join([str(l) for l in [i, j, k]]))
#             waterwind_list.append([i, j, k])

# for i in range(max_x-1, max_x+2):
#     for j in range(max_y-1, max_y+2):
#         for k in range(max_z-1, max_z+2):
#             waterwind.add('/'.join([str(l) for l in [i, j, k]]))
#             waterwind_list.append([i, j, k])
            

# subset = set()
# subset_coords = []
# for cube in magma_coords: # [x, y, z]
#     position = cube[0], cube[1], cube[2]
    
#     right, left, forward, backwards, up, down = lookaround(position, cords=True)
    
#     for i in (right, left, forward, backwards, up, down):
#         x, y, z = i[0], i[1], i[2]
    
#         if (min_x < x < max_x) and (min_y < y < max_y) and (min_z < z < max_z):
#             pos = '/'.join([str(i) for i in [x, y, z]])
#             if pos not in magma_set:
#                 subset.add(pos)
#             if [x, y, z] not in magma_coords:
#                 subset_coords.append([x, y, z])
                
