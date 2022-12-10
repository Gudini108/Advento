import os
import sys

import numpy as np

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    forest = f.read().split('\n')
    

    
    
forest_lines = []
for line in forest:
    line_list = []
    for tree in line:
        line_list.append(int(tree))
    forest_lines.append(line_list)
    
forest_matrix = np.array(forest_lines)


copyforest = forest.copy()


for i in range(len(copyforest)):
    copyforest[i] = list(copyforest[i])
    

for row_num in range(len(copyforest)):
    row = copyforest[row_num]
    
    for num in enumerate(row): 
        col_num = num[0]
        height = num[1]
        
        coordinates = {'height': int(height), 'is_visible': False, 'scenic_score': 1} # [<number>, <its row>, <its pos in row (aka col number)>]
        
        copyforest[row_num][col_num] = coordinates

copyforest_matrix = np.array(copyforest)

# copyforest_matrix[0][0]['name'] --> copyforest_matrix[row][element][number, row or column]

matrix_slice = copyforest_matrix[:3, :3]



rotations = 0
visible_trees = 0
while rotations != 4: # make 4 rotations and stop
    
    for row in range(len(copyforest_matrix)):
        heighest_tree_height = -1 # we start at -1 because there are no trees outside of forest grid
        
        tree_dict = {}
        
        for tree_info in enumerate(copyforest_matrix[row]):
            tree = tree_info[1]
            tree_index = tree_info[0]

            current_tree_height = tree['height'] # height of the tree (its number from 0 to 9)
            
            if current_tree_height > heighest_tree_height:
                heighest_tree_height = current_tree_height
                tree_dict[current_tree_height] = tree_index
                
                if tree['is_visible'] == False:
                    tree['is_visible'] = True
                    visible_trees += 1
                    
                           
    copyforest_matrix = np.rot90(copyforest_matrix) # rotate our matrix 90 degrees counterclockwise
    rotations += 1 # indicate one rotation

        
print(visible_trees) # final result minus 4 corners that we already counted while turning our matrix