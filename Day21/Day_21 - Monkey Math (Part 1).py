import os
import sys

with open(os.path.join(sys. path[0], "input.txt"), "r") as f:
    monkey_talk = f.read().split('\n')
    
while 'root' not in locals():
    for scream in monkey_talk:
        var, result = scream.split(': ')
        try:
            locals()[var] = eval(result)
        except NameError:
            pass
        
print(root)