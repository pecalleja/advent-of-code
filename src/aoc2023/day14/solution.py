from aoc2023 import Solution


class Day14Solution(Solution):
    def result(self):
        raise NotImplementedError

    def convert_array(self):
        self.data = [[c for c in row] for row in self.data]

    def move_rocks(self):
        self.convert_array()
        r, c = len(self.data), len(self.data[0])
        for i in range(r):
            for _ in range(c):
                for j in range(c):
                    cell = self.data[j][i]
                    if cell == "O" and j > 0 and self.data[j - 1][i] == ".":
                        self.data[j][i] = "."
                        self.data[j - 1][i] = "O"


class Part1Solution(Day14Solution):
    def result(self):
        self.move_rocks()
        r = len(self.data)
        return sum(row.count("O") * (r - i) for i, row in enumerate(self.data))


class Part2Solution(Day14Solution):
    def result(self):
        return None
