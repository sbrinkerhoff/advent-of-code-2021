
import sys
input = list(map(lambda x: int(x), open(sys.argv[1], 'r').read().split(",")))

# count number in each position
pos = {}
for x in input:
    pos[x] = pos.get(x,0) + 1

options = range(1, max(pos.keys()))
results = {}

for option in options:
    # option will be target number to moe the pos to.
    fuel = 0
    for key, value in pos.items():
        fuel += abs(key-option) * value
    results[option] = fuel
    
print(results)
print(min(results.values()))
    