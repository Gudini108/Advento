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
        

sidecounter = 0
for cube in magma_coords:
    x, y, z = cube[0], cube[1], cube[2]
    
    x_pos = '/'.join(str(i) for i in [x+1, y, z])
    x_neg = '/'.join(str(i) for i in [x-1, y, z])
     
    y_pos = '/'.join(str(i) for i in [x, y-1, z])
    y_neg = '/'.join(str(i) for i in [x, y+1, z])
    
    z_pos = '/'.join(str(i) for i in [x, y, z+1])
    z_neg = '/'.join(str(i) for i in [x, y, z-1])
    
    neighbours = (x_pos, x_neg, y_pos, y_neg, z_pos, z_neg)
    
    for pos in neighbours:
        if pos not in magma_set:
            sidecounter += 1

print(sidecounter)