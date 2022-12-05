import os
import sys
import string
import re

with open(os.path.join(sys.path[0], "crates.txt"), "r") as f:
    
    crates = f.read().split('\n')[0:-1]

with open(os.path.join(sys.path[0], "moves.txt"), "r") as f:
    
    moves = f.read().split('\n')



def linemaker(pos):
    position = {1:1, 2:5, 3:9, 4:13, 5:17, 6:21, 7:25, 8:29, 9:33}
    pos = position[pos]
    line = []
    for row in range(8):
        if crates[row][pos] in string.ascii_uppercase:
            line.append(crates[row][pos])
    return line

i = 1
lines = {}
while i <= 9:
    lines[i] = linemaker(i)
    i += 1


for move in moves:
    crates_num, from_where, to_where = [int(x) for x in re.findall('\d+', move)]
    
    from_line = lines[from_where] # chooses a line from where we will take our crates
    to_line = lines[to_where] # chooses a line to where we will send our crates
    
    for crate in range(crates_num): # take one by one crate from one line and send to another
        to_line.insert(0, from_line[crate]) # insert crate from other line to destination in 1st position
        
    for crate in range(crates_num):
        from_line.pop(0)
    

print (''.join([lines[x][0] for x in range(1, 10)])) # 1st answer



i = 1
lines = {}
while i <= 9:
    lines[i] = linemaker(i)
    i += 1

for move in moves:
    crates_num, from_where, to_where = [int(x) for x in re.findall('\d+', move)]
    
    from_line = lines[from_where] # chooses a line from where we will take our crates
    to_line = lines[to_where] # chooses a line to where we will send our crates
    
    CrateMover_9001 = []
    for crate in range(crates_num): # take one by one crate from one line and send to CrateMover_9001
        CrateMover_9001.append(from_line[crate]) 
    
    CrateMover_9001 = CrateMover_9001[::-1] # reverse CrateMover_9001 (he can do that, right? It's new awesome CrateMover 9001!)
    for crate in range(crates_num):
        to_line.insert(0, CrateMover_9001[crate]) # add crates to new line
       
    for crate in range(crates_num): # remove extra crates
        from_line.pop(0)
        

print (''.join([lines[x][0] for x in range(1, 10)])) # 2nd answer