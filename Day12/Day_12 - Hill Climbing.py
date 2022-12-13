import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    valley = f.read().split('\n')
    
import string
    

enumerated_letters = dict(enumerate((string.ascii_lowercase), start=1))
enumerated_letters = {v:k for (k,v) in enumerated_letters.items()}


elevation = []
final_destination = None
for index, line in enumerate(valley):
    new_line = []
    
    for letter_index, letter in enumerate(list(line)):
        
        if letter == 'S':
            new_line.append({'height': 1, 'is_visited': False})
            
        if letter == 'E':
            final_destination = index, letter_index
            new_line.append({'height': 27, 'is_visited': False})
            
        if letter in list(string.ascii_lowercase):
            new_line.append({'height': int(enumerated_letters[letter]), 'is_visited': False})
            
    elevation.append(new_line)



def get_valid_position(next_row, next_col, current_element, path_length):
    
    next_element = elevation[next_row][next_col]
        
    if (current_element['height'] - next_element['height']) < 2:
        
        if not next_element['is_visited']:
            
            next_element['is_visited'] = True
        
            return [next_row, next_col, path_length+1]
    


queue = [[20, 148, 0]]

while len(queue) != 0:
    
    row, col, path_length = queue.pop(0)
    
    current_element = elevation[row][col]
    
    
    if col < len(elevation[0]) - 1: # right
        
        valid = get_valid_position(row, col+1, current_element, path_length)
        
        if valid:
            queue.append(valid)
        
    
    if col > 0: # left 
        
        valid = get_valid_position(row, col-1, current_element, path_length)
        
        if valid:
            queue.append(valid)
    
    
    if row > 0: # up
        
        valid = get_valid_position(row-1, col, current_element, path_length)
        
        if valid:
            queue.append(valid)
    
    
    if row < len(elevation) - 1: # down
        
        valid = get_valid_position(row+1, col, current_element, path_length)
        
        if valid:
            queue.append(valid)
    
    
    if current_element['height'] == 1:
        print(f'Path length: {path_length}')
        break