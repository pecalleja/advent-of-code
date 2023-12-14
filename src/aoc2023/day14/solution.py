from aoc2023 import Solution


class Day14Solution(Solution):
    def result(self):
        raise NotImplementedError

    def move_rocks_north(self, grid):
        result = [
            [e for e in f] for f in grid
        ]  # do not modify the original object
        r, c = len(result), len(result[0])
        for i in range(r):
            for _ in range(c):
                for j in range(c):
                    cell = result[j][i]
                    if cell == "O" and j > 0 and result[j - 1][i] == ".":
                        result[j][i] = "."
                        result[j - 1][i] = "O"
        return result

    def rotate_grid(self, grid):
        result = [[e for e in f] for f in grid]
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                result[j][r - 1 - i] = grid[i][j]
        return tuple(map("".join, result))

    def calculate(self, grid):
        r = len(grid)
        return sum(row.count("O") * (r - i) for i, row in enumerate(grid))


class Part1Solution(Day14Solution):
    def result(self):
        result = self.move_rocks_north(self.data)
        return self.calculate(result)


class Part2Solution(Day14Solution):
    def result(self):
        cache = {}
        target = 10**9
        t = 0
        grid = self.data
        while t < target:
            t += 1
            for j in range(4):
                grid = self.move_rocks_north(grid)
                grid = self.rotate_grid(grid)
            if grid in cache:
                cycle_length = t - cache[grid]
                amt = (target - t) // cycle_length
                t += amt * cycle_length
            cache[grid] = t
        return self.calculate(grid)
