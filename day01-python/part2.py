class SlidingWindow:
    items: list = []

    def add(self, item: int) -> None:
        self.items.append(item)
        if len(self.items) > 3:
            self.items.pop(0)

    def sum(self) -> int:
        return sum(self.items)


def calculate_increases(inputs: list) -> int:
    depth = inputs[0]
    increases = 0

    for i in inputs:
        if i > depth:
            increases += 1
        depth = i

    return increases


def read_inputs(f="../inputs/day01.txt") -> list:
    inputs = open(f, "r").readlines()
    inputs = [int(x.strip()) for x in inputs]
    return inputs


def main():
    inputs = read_inputs()
    sw = SlidingWindow()
    sums = []
    for i in inputs:
        sw.add(i)

        if len(sw.items) == 3:
            sums.append(sw.sum())

    print(calculate_increases(sums))


if __name__ == "__main__":
    main()
