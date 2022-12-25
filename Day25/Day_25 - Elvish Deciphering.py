import os
import sys

with open(os.path.join(sys. path[0], "input.txt"), "r") as f:
    cypher = f.read().split('\n')
    
def decypheringer(code: str) -> int:
    code = code[::-1]
    result = 0
    for i in range(len(code)):
        if code[i] in ['0', '1', '2']:
            result += (5**i) * int(code[i])

        if code[i] == '-':
            result += (5**i) * -1

        if code[i] == '=':
            result += (5**i) * -2

    return result

def redecypheringer(numcode: int) -> str:
    SNAFU = []
    while numcode:
        numcode, left = divmod(numcode, 5)
        if left == 3:
            numcode += 1
            left = '='
        elif left == 4:
            numcode += 1 
            left = '-'
        SNAFU.append(left)
    return (''.join([str(digit) for digit in SNAFU[::-1]]))
            
            
great_result = 0
for code in cypher:
    great_result += decypheringer(code)

print(great_result)
print(redecypheringer(great_result))
print(decypheringer(str(redecypheringer(great_result))))