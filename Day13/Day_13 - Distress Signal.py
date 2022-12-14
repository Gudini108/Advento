import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    pairs_input = f.read().split('\n')
    
from functools import cmp_to_key

evaluated_lines = []
for line in range(len(pairs_input)):
    if pairs_input[line] != '':
        evaluated_lines.append(eval(pairs_input[line]))
        
       
evaluated_lines_copy = evaluated_lines.copy()


def comparing_numbers(a, b):
    
    for left, right in zip(range(len(a)), range(len(b))):
        
        a_left, b_right = [a[left], b[right]]
        
        if isinstance(a_left, int) and isinstance(b_right, int):
            
            if a_left < b_right:
                return 1
            
            if a_left > b_right:
                return -1
    
        else:
            
            if isinstance(a_left, int) and isinstance(b_right, list):
                a_left = [a_left]
                
            if isinstance(a_left, list) and isinstance(b_right, int):
                b_right = [b_right]
            
            if isinstance(a_left, list) and isinstance(b_right, list):
                result =  comparing_numbers(a_left, b_right)
                
                if result == None:
                    continue
                
                else:
                    return result
            
        
    if len(a) > len(b):
        return -1
    
    if len(a) < len(b):
        return 1
    
    else:
        return None
    
indices = 0
for line in range(len(evaluated_lines_copy)): 
    if line % 2 == 0:
        if comparing_numbers(evaluated_lines_copy[line], evaluated_lines_copy[line+1]) == 1:
           indices += line/2 + 1
           

evaluated_lines_copy.append([[2]])
evaluated_lines_copy.append([[6]])

evaluated_copy_sorted = sorted(evaluated_lines_copy, key=cmp_to_key(comparing_numbers), reverse=True)

print(int(indices))

sorted_anum = list(enumerate(evaluated_copy_sorted, start=1))

cool_indeces = 1
for pair in sorted_anum:
    if pair[1] == [[2]] or pair[1] == [[6]]:
        cool_indeces *= pair[0]

print(cool_indeces)