#!/usr/bin/env python3

import sys

from multiprocessing.pool import ThreadPool

def fishy_thread(days,inputs,results,id):

    for x in range(0,days):
        print(f"Thread {id} day {x}, Fish: {len(next_day_fish)}")
        school = next_day_fish
        next_day_fish = []
        for fish in school:
            try:
                fish.decrement()
            except:
                fish.current=8
                next_day_fish.append(Fish(6)) # the existing fish
            finally:
                next_day_fish.append(fish)
                
    results[id] = len(next_day_fish)
    
class Fish:
    def __init__(self,current=8):
        self.current = current
    def decrement(self):
        self.current -= 1
        if self.current < 0:
            raise Exception("Fish out of bounds")

inputs = open(sys.argv[1], 'r').read().split(",")

# Create a school
school = [Fish(int(i)) for i in inputs]



days = 256

next_day_fish = school

for x in range(0,days):
    print(f"Day {x}, Fish: {len(next_day_fish)}")
    school = next_day_fish
    next_day_fish = []
    for fish in school:
        try:
            fish.decrement()
        except:
            fish.current=8
            next_day_fish.append(Fish(6)) # the existing fish
        finally:
            next_day_fish.append(fish)

print(len (next_day_fish))