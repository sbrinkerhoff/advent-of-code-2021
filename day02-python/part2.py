
def read_inputs(f="../inputs/day02.txt") -> list:
    inputs = open(f, "r").readlines()
    inputs = [x.strip() for x in inputs]
    return inputs

i = read_inputs()

loc = 0
aim = 0
depth = 0
for line in i:
    cmd, qty = line.split(" ")
    print(cmd,qty)
    if cmd == "forward":
        loc += int(qty)
        depth += aim*int(qty)
    if cmd == "down":
        aim += int(qty)
    if cmd == "up":
        aim -= int(qty)

print(loc*depth)