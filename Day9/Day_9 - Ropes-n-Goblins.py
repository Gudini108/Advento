import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    directions = f.read().split('\n')


visited_positions = set()

rope_segments = []
rope_length = 10

for segment in range(0, rope_length):
    rope_segments.append({'position': [0, 0]})


for move in directions:
    
    split_move = move.split(' ')
    move_where = split_move[0]
    move_steps = int(split_move[1])
        
    for step in range(move_steps):
        temporal_afterimage = []
        
        for segment_num in range(rope_length):
            
            current_segment = rope_segments[segment_num]['position']
            previous_segment = rope_segments[segment_num - 1]['position']
            
            
            if segment_num == 0:
                    
                temporal_afterimage = current_segment[:]
                
                
                if move_where == 'R':
                    current_segment[1] += 1
                    
                elif move_where == 'L':
                    current_segment[1] -= 1
                    
                elif move_where == 'U':
                    current_segment[0] += 1
                    
                else:
                    current_segment[0] -= 1
                    
            
            else:
                
                left_axis_difference = previous_segment[0] - current_segment[0]
                left_axis_difference_modulus = abs(left_axis_difference)
                
                right_axis_difference = previous_segment[1] - current_segment[1]
                right_axis_difference_modulus = abs(right_axis_difference)

                
                if (left_axis_difference_modulus >= 2) or (right_axis_difference_modulus >= 2):
                        
                    if left_axis_difference != 0:
                        rope_segments[segment_num]['position'][0] += int(left_axis_difference/left_axis_difference_modulus)
                            
                    if right_axis_difference != 0:
                        rope_segments[segment_num]['position'][1] += int(right_axis_difference/right_axis_difference_modulus)
                
                temporal_afterimage = current_segment[:]
                
        visited_positions.add('/'.join(str(x) for x in rope_segments[-1]['position']))
             

print(len(visited_positions))