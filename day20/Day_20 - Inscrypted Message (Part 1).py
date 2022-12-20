import os
import sys

with open(os.path.join(sys. path[0], "input.txt"), "r") as f:
    inscryption = f.read().split('\n')
    
indexoid = list(enumerate(inscryption))

copy_indexoid = indexoid.copy()

for i in range(len(indexoid)):  
    
    pair = copy_indexoid[i]
        
    if int(pair[1]) != 0:

        pair_index = indexoid.index(pair)
        pair_number = int(pair[1])
            
        move_score = pair_index + pair_number
        
        while move_score > len(indexoid)-1:
            move_score -= len(indexoid)-1

        while move_score <= 0:
            move_score += len(indexoid)-1

        indexoid.remove(pair)
        indexoid.insert(move_score, pair)
                    

coordinate = 0
numbers = []
for i in indexoid:
    if int(i[1]) == 0:
        
        zero_index = indexoid.index(i)
        
        first_move = zero_index + 1000
        second_move = zero_index + 2000
        third_move = zero_index + 3000
        
        first_index = first_move%len(indexoid)
        second_index = second_move%len(indexoid)
        third_index = third_move%len(indexoid)
        
        numbers.append(int(indexoid[first_index][1]))
        numbers.append(int(indexoid[second_index][1]))
        numbers.append(int(indexoid[third_index][1]))
        
            
print(numbers)
print(sum(numbers))