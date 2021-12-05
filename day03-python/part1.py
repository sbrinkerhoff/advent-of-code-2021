#!/usr/bin/env python3

i = [x.strip() for x in open("../inputs/day03.txt", "r").readlines()]

gamma = ""
ep = ""

for ct in range(len(i[0])):
    val = 0
    
    for x in i:
        val += int(x[ct])
    
    gamma += "1" if (int(val>len(i)-val)) else "0"
    ep += "0" if (int(val>len(i)-val)) else "1"
    
print(int(gamma,2), int(ep,2))
print(int(gamma,2)*int(ep,2))

#2981
#1114