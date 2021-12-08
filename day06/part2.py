#!/usr/bin/env python3

import sys

    
def fish_two(days, inputs):
    fish_timers = {}
    
    new_fish_timers = {}
    
    for i in inputs:
        fish_timers[i] = fish_timers.get(i,0) + 1
    
    for day in range(days):
        print(f"Day {day} Fish: {fish_timers} Sum: {sum(fish_timers.values())}")
        
        for x in range(0,9):
            #print(f"id {x}")
            new_fish_timers[x-1] = fish_timers.get(x,0)
            
        new_fish_timers[6] += new_fish_timers.get(-1,0)
        new_fish_timers[8] = new_fish_timers.get(-1,0)
        new_fish_timers[-1] = 0
        fish_timers = new_fish_timers        
        
    
    return sum(fish_timers.values())
    


if __name__ == "__main__": 
        
    
    fish_i = map(lambda x: int(x), open(sys.argv[1]).read().split(","))
    days = 256

    final = (fish_two(days, fish_i))
    print(final)
