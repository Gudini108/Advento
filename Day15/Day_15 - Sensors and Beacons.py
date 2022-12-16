import os
import sys

with open(os.path.join(sys. path[0], "input.txt"), "r") as f:
    sensors_and_beacons_positions = f.read().split('\n')
    
  
beacons_x_y = []    
sensor_width = []
for line in sensors_and_beacons_positions:
    
    line = line.split('at ')
    
    beacon_coords = line[2]
    beacon_x = int(beacon_coords.split(',')[0].split('=')[1])
    beacon_y = int(beacon_coords.split(',')[1].split('=')[1])
    
    sensor_coords = line[1].split(':')[0]
    sensor_x = int(sensor_coords.split(',')[0].split('=')[1])
    sensor_y = int(sensor_coords.split(',')[1].split('=')[1])
    
    sensor_left_most = sensor_x - (abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y))
    sensor_right_most = sensor_x + (abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y))
    
    sensor_width.append([sensor_left_most, sensor_right_most, sensor_y])
    
    if [beacon_x, beacon_y] not in beacons_x_y:
        beacons_x_y.append([beacon_x, beacon_y])
    

checking_y_row = 2000000

no_beacon_zone = []
for pair in sensor_width:
    
    step = abs(pair[2] - checking_y_row)
    
    new_range_start_x = pair[0] + step
    new_range_end_x = pair[1] - step
    
    if new_range_start_x <= new_range_end_x:
         no_beacon_zone.append([new_range_start_x, new_range_end_x])
    

sorted_beacons = sorted(no_beacon_zone)


clean_pairs = []
    
start = sorted_beacons[0][0]
end = sorted_beacons[0][1]

for pair in range(len(sorted_beacons)):
    
    if pair != len(sorted_beacons) - 1:
        
        start_2 = sorted_beacons[pair + 1][0]
        end_2 = sorted_beacons[pair + 1][1]
        
        if start <= start_2 <= end and not start <= end_2 <= end:
            end = end_2
        
        elif (not start < start_2 <= end):
            clean_pairs.append([start, end])
            start = start_2
            end = end_2
    
    else:
        clean_pairs.append([start, end])
    

no_beacon_spaces = 0 + len(clean_pairs)
for pair in clean_pairs:
    no_beacon_spaces += pair[1] - pair[0]
    for beacon in beacons_x_y:
        if beacon[1] == checking_y_row:
            if pair[0] <= beacon[0] <= pair[1]:
                no_beacon_spaces -= 1


print(no_beacon_spaces)

starting_range = 0
ending_range = 4000000

row_counter = 0
for checking_y_row in range(starting_range, ending_range):

    no_beacon_zone = []
    for pair in sensor_width:
        
        step = abs(pair[2] - checking_y_row)
        
        new_range_start_x = pair[0] + step
        new_range_end_x = pair[1] - step
        
        if new_range_start_x <= new_range_end_x:
            no_beacon_zone.append([new_range_start_x, new_range_end_x])
        

    sorted_beacons = sorted(no_beacon_zone)


    clean_pairs = []
        
    start = sorted_beacons[0][0]
    end = sorted_beacons[0][1]

    for pair in range(len(sorted_beacons)):
        
        if pair != len(sorted_beacons) - 1:
            
            start_2 = sorted_beacons[pair + 1][0]
            end_2 = sorted_beacons[pair + 1][1]
            
            if start <= start_2 <= end and not start <= end_2 <= end:
                end = end_2
            
            elif (not start < start_2 <= end):
                clean_pairs.append([start, end])
                start = start_2
                end = end_2
        
        else:
            clean_pairs.append([start, end])
    
    
    if len(clean_pairs) == 2:
        x_coord = clean_pairs[0][1] + 1
        y_coord = row_counter
    
    else:
        row_counter += 1
        

print(x_coord * 4000000 + y_coord)