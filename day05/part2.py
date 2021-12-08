#!/usr/bin/env python


class Vents:
    def __init__(self):
        self.grid = []
        for x in range(1000):
            self.grid.append([0] * 1000)

    def add(self, x1, y1, x2, y2):
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        if x1 == x2:
            if y1 > y2:
                for y in range(y2, y1 + 1):
                    print(f"{x1},{y}")
                    self.add_grid(x1, y)
            else:
                for y in range(y1, y2 + 1):
                    print(f"{x1},{y}")
                    self.add_grid(x1, y)

        elif y1 == y2:
            if x1 > x2:
                for x in range(x2, x1 + 1):
                    self.add_grid(x, y1)
            else:
                for x in range(x1, x2 + 1):
                    self.add_grid(x, y1)

        else:  # diagonal
            print(f"Diagonal -> {x1} {y1} -> {x2} {y2}")

            if x1 < x2:
                if y1 < y2:
                    while x2 >= x1:
                        self.add_grid(x1, y1, True)
                        x1 += 1
                        y1 += 1
                if y1 > y2:
                    while x2 >= x1:
                        self.add_grid(x1, y1, True)
                        x1 += 1
                        y1 -= 1

            elif x1 > x2:
                if y1 < y2:
                    while x2 <= x1:
                        self.add_grid(x1, y1, True)
                        x1 -= 1
                        y1 += 1
                if y1 > y2:
                    while x2 <= x1:
                        self.add_grid(x1, y1, True)
                        x1 -= 1
                        y1 -= 1

    def add_grid(self, x, y, output=False):
        if output:
            print(f"Adding to grid: {x},{y}")
        self.grid[y][x] = self.grid[y][x] + 1

    def get_cell(self, x, y):
        return self.grid[y][x]


def main():
    lines = [x.strip() for x in open("input", "r").readlines()]
    # lines = [x.strip() for x in open("test", "r").readlines()]

    v = Vents()

    for line in lines:
        print(line)
        x, y = line.split("->")
        v.add(*x.strip().split(","), *y.strip().split(","))

    ct = 0
    for x in v.grid:
        for y in x:
            if y > 1:
                ct += 1

    print(ct)


if __name__ == "__main__":
    main()
