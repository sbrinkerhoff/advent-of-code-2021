
def read_inputs(f="../inputs/day02.txt") -> list:
    inputs = open(f, "r").readlines()
    inputs = [x.strip() for x in inputs]
    return inputs

i = read_inputs()

loc = 0
dep = 0

for line in i:
    cmd, qty = line.split(" ")
    print(cmd,qty)
    if cmd == "forward":
        loc += int(qty)
    if cmd == "down":
        dep += int(qty)
    if cmd == "up":
        dep -= int(qty)

print(loc*dep)