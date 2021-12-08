
import sys
import math
input = list(map(lambda x: int(x), open(sys.argv[1], 'r').read().split(",")))

# count number in each position
pos = {}
for x in input:
    pos[x] = pos.get(x,0) + 1

options = range(1, max(pos.keys())+1)
results = {}

for option in options:
    # option will be target number to moe the pos to.
    fuel = 0
    print(f"Testing option: {option}")
    for key, value in pos.items():
        distance = abs(key-option)
        
        cost = 0
        for x in range(1,distance+1):
            cost += x
        #print(f"{key} -> {distance} (cost: {cost})")
        fuel += cost*value
        
    results[option] = fuel
    
print(results)
print(min(results.values()))
    