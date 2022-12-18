import os
import sys

with open(os.path.join(sys. path[0], "input.txt"), "r") as f:
    wind_directions = list(f.read())

current_floor_row = -1
floor_width = 7
left_wall = -1
right_wall = 7

shapes = ['vertline', 'cross', 'L-shape', 'horline', 'square']

settled_rocks = set()

for i in range(floor_width):
    settled_rocks.add('/'.join(str(x) for x in [i, -1]))

rocks_required = 1000000000000

def get_shape(shape): # get several [x, y] coordinates for different shapes
    
    if shape == 'vertline':
        shape_coords = [
            [left_wall + 3, current_floor_row + 4], 
            [left_wall + 4, current_floor_row + 4],
            [left_wall + 5, current_floor_row + 4],
            [left_wall + 6, current_floor_row + 4]]
    
    if shape == 'cross':
        shape_coords = [
            [left_wall + 3, current_floor_row + 5], # left part
            [left_wall + 4, current_floor_row + 4], # lower part of the cross
            [left_wall + 5, current_floor_row + 5], # right part
            [left_wall + 4, current_floor_row + 6]] # upper part of the cross
    
    if shape == 'L-shape':
        shape_coords = [
            [left_wall + 3, current_floor_row + 4], # outer left
            [left_wall + 4, current_floor_row + 4], # second left 
            [left_wall + 5, current_floor_row + 4], # angle
            [left_wall + 5, current_floor_row + 5], # angle up
            [left_wall + 5, current_floor_row + 6]] # upper part
        
    if shape == 'horline':
        shape_coords = [
            [left_wall + 3, current_floor_row + 4], 
            [left_wall + 3, current_floor_row + 5],
            [left_wall + 3, current_floor_row + 6],
            [left_wall + 3, current_floor_row + 7]] # upper part
        
    if shape == 'square':
        shape_coords = [
            [left_wall + 3, current_floor_row + 4], # left down
            [left_wall + 4, current_floor_row + 4], # right down
            [left_wall + 3, current_floor_row + 5], # left up
            [left_wall + 4, current_floor_row + 5]] # right up
    
    return shape_coords
    

shape_id = 0
for rock in range(rocks_required):
    rock_shape = get_shape(shapes[shape_id])
    
    for direction in wind_directions:
            
        if direction == '<': # if wind blows to the left
            shape_check = 0
            is_blocked = False
            
            while shape_check != len(rock_shape):
                
                for seg in range(len(rock_shape)):
                    segment = rock_shape[seg]
                    
                    if ((segment[0]-1 != left_wall) 
                        and (('/'.join(str(x) for x in [segment[0]-1, segment[1]])) not in settled_rocks)):
                        
                        shape_check += 1
                        
                    else:
                        shape_check += 1
                        is_blocked = True
                        
            
            if is_blocked == False:
                for seg in range(len(rock_shape)):
                    rock_shape[seg][0] -= 1          
        
        else: # if wind blows to the right
            shape_check = 0
            is_blocked = False
            
            while shape_check != len(rock_shape):
                
                for seg in range(len(rock_shape)):
                    segment = rock_shape[seg]
                    
                    if ((segment[0]+1 != right_wall) 
                        and ('/'.join(str(x) for x in [segment[0]+1, segment[1]]) not in settled_rocks)):
                        
                        shape_check += 1
                        
                    else:
                        shape_check += 1
                        is_blocked = True

            
            if is_blocked == False:
                for seg in range(len(rock_shape)):
                    rock_shape[seg][0] += 1
            
        
        wind_directions = wind_directions[::-1]
        wind_switcheroo = wind_directions.pop()
        wind_directions = wind_directions[::-1]
        wind_directions.append(wind_switcheroo)
        
        
        # check if we can go down further or is it time to settle
        shape_check = 0
        is_blocked = False
        while shape_check != len(rock_shape):
            
            for seg in range(len(rock_shape)):
                segment = rock_shape[seg]
                
                if '/'.join(str(x) for x in [segment[0], segment[1]-1]) not in settled_rocks:
                    shape_check += 1
                    
                else:
                    shape_check += 1
                    is_blocked = True
    
        
        if is_blocked == False: # if we are not blocked by anything down the road - advance further
            for seg in range(len(rock_shape)):
                rock_shape[seg][1] -= 1
    
        
        else: # if we are blocked by anything - settle instead
            
            if rock_shape[-1][1] > current_floor_row:
                current_floor_row = rock_shape[-1][1]
            
            is_settled = True
            
            for seg in range(len(rock_shape)): # add our coordinated to the database
                segment = rock_shape[seg]
                settled_rocks.add('/'.join(str(x) for x in [segment[0], segment[1]]))
            break
                
        
    # advance our shapes to the next one
    if shape_id == 4:
        shape_id = 0
    else:
        shape_id += 1
    
print(current_floor_row + 1)