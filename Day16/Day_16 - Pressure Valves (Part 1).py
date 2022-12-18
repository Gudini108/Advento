import os
import sys

with open(os.path.join(sys. path[0], "input.txt"), "r") as f:
    valves = f.read().split('\n')

valves_n_tunnels = {}

for line in valves:
    
    valve_name = line.split(' ')[1]
    pressure_rate = line.split(' ')[4].split(';')[0].split('=')[1]
    tunnels = line.split('valv')[1].split(' ')[1:]
    real_tunnels = []
    if len(tunnels) > 1:
        for tunnel in tunnels:
            real_tunnels.append(tunnel.split(',')[0])
    else:
        real_tunnels = tunnels
    
    valves_n_tunnels[valve_name] = {'pressure': int(pressure_rate), 'tunnels': real_tunnels}
    
            
vent_copy = valves_n_tunnels.copy()

closed_values = set()

for tunnel in vent_copy:
    if vent_copy[tunnel]['pressure'] > 0:
        closed_values.add(tunnel)
        

memo = {}

elememo = {}


def pathfinder(valve_system, starting_valve, countdown, closed_valves):
    
    current_tunnel = valve_system[starting_valve]
    
    key = '/'.join([starting_valve, str(countdown), str(closed_valves)])
    
    if key in memo:
        return memo[key]
    
    # print('closed values:', closed_valves, 'key:', key)
    
    if countdown == 0 or len(closed_valves) == 0:
        return 0
    
    best_tunnel_result = 0
    
    for tunnel in current_tunnel['tunnels']:
        copycats = closed_valves.copy()
        best_tunnel_result = max(pathfinder(valve_system, tunnel, countdown - 1, copycats), best_tunnel_result)
       
    if (current_tunnel['pressure'] > 0) and (starting_valve in closed_valves):
        copycats = closed_valves.copy()
        copycats.remove(starting_valve)
        result = pathfinder(valve_system, starting_valve, countdown - 1, copycats) + (countdown - 1) * current_tunnel['pressure']
        best_tunnel_result = max(result, best_tunnel_result)
        
    memo[key] = best_tunnel_result
    
    return best_tunnel_result



print( pathfinder(vent_copy, 'AA', 30, closed_values) )