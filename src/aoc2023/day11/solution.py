from itertools import combinations

from aoc2023 import Solution


class Day11Solution(Solution):
    expanded_universe: list[tuple] = []

    def result(self):
        raise NotImplementedError

    def expand_universe(self):
        def expand(data):
            expanded = []
            for item in data:
                expanded.append(item)
                if item.count("#") == 0:
                    expanded.append("." * len(item))
            return expanded

        expanded_row = expand(self.data)
        expanded_col = expand(list(zip(*expanded_row)))
        self.expanded_universe = list(zip(*expanded_col))


class Part1Solution(Day11Solution):
    universe: list[tuple] = []

    def result(self):
        self.expand_universe()
        for i, row in enumerate(self.expanded_universe):
            for j, cell in enumerate(row):
                if cell == "#":
                    self.universe.append((i, j))

        result = sum(
            abs(a[0] - b[0]) + abs(a[1] - b[1])
            for a, b in combinations(self.universe, 2)
        )
        return result


class Part2Solution(Day11Solution):
    def result(self):
        return None
