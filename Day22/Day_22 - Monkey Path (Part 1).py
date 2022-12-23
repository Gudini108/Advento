import os
import sys

with open(os.path.join(sys. path[0], "map.txt"), "r") as f:
    map = f.read().split('\n')

with open(os.path.join(sys. path[0], "moves.txt"), "r") as f:
    moves = f.read()
    
    
import time

    
movelist = []
numberfile = []
for i in range(len(list(moves))):
    
    char = moves[i]
    
    if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        numberfile.append(char)
            
    else:
        
        if len(numberfile) > 0:
            numbers = ''.join(x for x in numberfile)
            movelist.append(int(numbers))
            numberfile.clear()
        
        movelist.append(char)
        
            
if len(numberfile) > 0:
    numbers = ''.join(x for x in numberfile)
    movelist.append(int(numbers))
    numberfile.clear()      
        

listed_map = []
for i in map:
    listed_map.append(list(i))

    
row = 0
col = 0
for i in listed_map[0]:
    if i == '.':
        break
    col += 1



def change_direction(facing, rotation) -> str: # change facing depending on rotation
    
    if rotation == 'R': # if we rotate clockwise
        
        if facing == '>':
            facing = 'v'
            
        elif facing == 'v':
            facing = '<'
            
        elif facing == '<':
            facing = '^'
            
        else:
            facing = '>'
    
    else: # if we rotate counterclockwise
        
        if facing == '>':
            facing = '^'
            
        elif facing == '^':
            facing = '<'
            
        elif facing == '<':
            facing = 'v'
            
        else:
            facing = '>'
    
    return facing

def move_accordingly(row, col, facing) -> tuple[int, int]:
    if facing == '>':
        row += 0
        col += 1
    elif facing == '<':
        row += 0
        col -= 1
    elif facing == '^':
        row -= 1
        col += 0
    else:
        row += 1
        col += 0
    
    return row, col

def check_for_obstacles(current_row, current_col, current_facing) -> tuple[int, int]:
    next_row, next_col = move_accordingly(current_row, current_col, current_facing)

    if (0<= next_row < len(listed_map)) and (0 <= next_col < len(listed_map[next_row])):
        
        
        obstacle = listed_map[next_row][next_col]
        
        print(next_row+1, next_col+1, 'obstacle ->', obstacle)
        
        if obstacle == '#':
            return current_row, current_col
        
        elif obstacle == '.':
            return next_row, next_col
        

    if current_facing == '>':

        for i in range(len(listed_map[current_row])):
            
            if listed_map[current_row][i] == '#':
                return current_row, current_col
            
            if listed_map[current_row][i] == '.':
                current_col = i
                break
                
                
    if current_facing == '<':

        for i in range(len(listed_map[current_row])-1, -1, -1):
            
            if listed_map[current_row][i] == '#':
                return current_row, current_col
            
            if listed_map[current_row][i] == '.':
                current_col = i
                break
                    
        
    if current_facing == '^':

        for i in range(len(listed_map)-1, -1, -1):
            
            if len(listed_map[i]) <= current_col:
                continue
            
            elif listed_map[i][current_col] == '#':
                return current_row, current_col
            
            elif listed_map[i][current_col] == '.':
                current_row = i
                break
                
    
    if current_facing == 'v':

        for i in range(len(listed_map)):
            
            if len(listed_map[i]) <= current_col:
                continue
            
            elif listed_map[i][current_col] == '#':
                return current_row, current_col
            
            elif listed_map[i][current_col] == '.':
                current_row = i
                break

    
    return current_row, current_col
    

current_facing = '>'
for move in movelist:
    
    if isinstance(move, int):
        
        for i in range(move):
            row, col = check_for_obstacles(row, col, current_facing)
    
    else:
        current_facing = change_direction(current_facing, move)


face_value = {'>': 0, 'v': 1, '<': 2, '^': 3}

code = (row+1) * 1000 + (col+1) * 4 + face_value[current_facing]

print(row+1, col+1, current_facing)
print(code)