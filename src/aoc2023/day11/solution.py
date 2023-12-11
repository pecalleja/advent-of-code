from itertools import combinations

from aoc2023 import Solution


class Day11Solution(Solution):
    universe: list[tuple]
    black_holes: dict[str, list]
    factor: int

    def __init__(self, data, factor):
        super().__init__(data)
        self.factor = factor

    def expand_universe(self):
        self.black_holes = {"row": [], "col": []}

        def expand(data, direction):
            for i, item in enumerate(data):
                if item.count("#") == 0:
                    self.black_holes[direction].append(i)

        expand(self.data, "row")
        expand(list(zip(*self.data)), "col")

    def map_galaxies(self):
        self.universe = []
        for i, row in enumerate(self.data):
            for j, cell in enumerate(row):
                if cell == "#":
                    self.universe.append((i, j))

    def get_black_holes(self, direction, *limits):
        lower_bound = min(limits)
        upper_bound = max(limits)
        return list(
            filter(
                lambda x: lower_bound <= x <= upper_bound,
                self.black_holes[direction],
            )
        )

    def result(self):
        self.expand_universe()
        self.map_galaxies()
        result = 0
        for a, b in combinations(self.universe, 2):
            expand_row = self.get_black_holes("col", a[1], b[1])
            expand_col = self.get_black_holes("row", a[0], b[0])
            result += (
                abs(a[0] - b[0])
                + (len(expand_row) * (self.factor - 1))
                + abs(a[1] - b[1])
                + (len(expand_col) * (self.factor - 1))
            )
        return result
