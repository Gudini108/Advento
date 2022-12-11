import os
import sys

import numpy as np

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    programm = f.read().split('\n')
    

register_X = 1

cycle = 0

cycle_checker = [20, 60, 100, 140, 180, 220]

signal_strength = 0

image = {'0-39':[], '40-79':[], '80-119':[], '120-159':[], '160-199':[], '200-239':[]}


picture_width = 40
picture_filler = '.'
for row in image:
    for symbol in range(picture_width):
        image[row].append(picture_filler)
    
pixel_count = 0


for instruction in programm:
    instruction = instruction.split(' ')
    code = instruction[0]
    operation_number = int(instruction[1]) if len(instruction) > 1 else None
    
    if code == 'noop':
        
        for row_name in image:
            split_name = row_name.split('-')
            row_start = int(split_name[0])
            row_end = int(split_name[1])

            if cycle >= row_start and cycle <= row_end:

                if pixel_count >= register_X - 1 and pixel_count <= register_X + 1:
                    image[row_name][pixel_count] = '#' 
            
            
        if pixel_count == 39:
            pixel_count = 0
        else:
            pixel_count += 1
            
        cycle += 1
        
        
        if (cycle in cycle_checker) and cycle == cycle_checker[0]:
            signal_strength += register_X * cycle
            cycle_checker.pop(0)
        
    
    else:
        
        for tick in range(2):
            
            for row_name in image:
                split_name = row_name.split('-')
                row_start = int(split_name[0])
                row_end = int(split_name[1])

                if cycle >= row_start and cycle <= row_end:

                    if pixel_count >= register_X - 1 and pixel_count <= register_X + 1:
                        image[row_name][pixel_count] = '#'
            
            
            if pixel_count == 39:
                pixel_count = 0
            else:
                pixel_count += 1
                
            cycle += 1
            
            
            if (cycle in cycle_checker) and cycle == cycle_checker[0]:
                signal_strength += register_X * cycle
                cycle_checker.pop(0)
            
        
        register_X += operation_number
                
        
print(signal_strength)

for row in image:
    print(''.join(image[row]))