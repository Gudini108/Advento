import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    monkeys = f.read().split('\n')

import math


band_of_monkeys = []

for line in range(len(monkeys)): # get them monkes
    
    if monkeys[line].startswith('Monkey', 0, len(monkeys[line])):
        monkey_number = monkeys[line].split(' ')[1][0]
        continue
    
    if monkeys[line].startswith('  Starting items', 0, len(monkeys[line])):
        starting_items_string = monkeys[line].split(': ')[1]
        starting_items = []
        
        for item in starting_items_string.split(', '):
            starting_items.append(int(item))
        continue
    
    if monkeys[line].startswith('  Operation', 0, len(monkeys[line])):
        operation_text = monkeys[line].split(': ')[1]
        operation_input = operation_text.split('= ')[1]
        continue
        
    if monkeys[line].startswith('  Test', 0, len(monkeys[line])):
        divider = int(monkeys[line].split('y ')[1])
        continue
    
    if monkeys[line].startswith('    If true', 0, len(monkeys[line])):
        true_monkey = monkeys[line].split(': ')[1]
        true_monkey_number = int(true_monkey.split('y ')[1])
        continue
    
    if monkeys[line].startswith('    If false', 0, len(monkeys[line])):
        false_monkey = monkeys[line].split(': ')[1]
        false_monkey_number = int(false_monkey.split('y ')[1])
        
        monke = [starting_items, [operation_input, divider, true_monkey_number, false_monkey_number], 0]
        band_of_monkeys.append(monke)
        

cumulative_test_divider = 1
for monkey in band_of_monkeys:
    cumulative_test_divider *= monkey[1][1]


def operation(old, operational_input, test_divider, monkey_friend_true, monkey_friend_false, worry_reduce = True):
    
    if worry_reduce:
        new_item = math.floor(eval(operational_input) / 3)
    
    else:
        new_item = eval(operational_input)
        new_item = new_item % cumulative_test_divider
    
    if new_item % test_divider == 0:
        monkey_to_pass = monkey_friend_true
    
    else:
        monkey_to_pass = monkey_friend_false
        
    return new_item, monkey_to_pass



number_of_rounds = 0

while number_of_rounds != 10000:

    for monke in band_of_monkeys:
        
        if len(monke[0]) > 0:
            
            while len(monke[0]) != 0:
            
                item_to_inspect = monke[0][0]       # takes first item from the list of items
                operational_input = monke[1][0]     # string with operation after "=" sign
                operational_divider = monke[1][1]   # divider that monkey will use to test an item
                true_monke = monke[1][2]            # if test is true - throw item to this mokey
                false_monke = monke[1][3]           # if false - to this instead
                
                new_item, monke_to_pass = (
                    
                    operation(item_to_inspect, operational_input, operational_divider, 
                              true_monke, false_monke, worry_reduce=False))
                
                monke[2] += 1 
                monke[0].pop(0)
                
                band_of_monkeys[monke_to_pass][0].append(new_item)

    number_of_rounds += 1
        

monke_counts = []
for monke in band_of_monkeys:
    monke_counts.append(monke[2])

monke_counts_sorted = sorted(monke_counts, reverse = True)

monkey_business = monke_counts_sorted[0] * monke_counts_sorted[1]

print(monkey_business)