from aoc2023 import Solution


class Day13Solution(Solution):
    def __init__(self, data, *args, **kwargs):
        super().__init__(data)
        self.groups = data.split("\n\n")

    def result(self):
        raise NotImplementedError

    def solve(self, lines, eq):
        for i in range(1, len(lines)):
            if eq(lines[i - 1:: -1], lines[i:]):
                return i
        return 0


class Part1Solution(Day13Solution):
    def result(self):
        def eq(x, y):
            n = min(len(x), len(y))
            return x[:n] == y[:n]

        return sum(
            100 * self.solve(lines := group.strip().splitlines(), eq)
            + self.solve(list(zip(*lines)), eq)
            for group in self.groups
        )


class Part2Solution(Day13Solution):
    def result(self):
        def eq(x, y):
            return sum(c != d for a, b in zip(x, y) for c, d in zip(a, b)) == 1

        return sum(
            100 * self.solve(lines := group.strip().splitlines(), eq)
            + self.solve(list(zip(*lines)), eq)
            for group in self.groups
        )
