from collections import deque

from aoc2023 import Solution


class Day21Solution(Solution):
    grid: list

    def result(self):
        raise NotImplementedError

    def parse_start(self):
        sr, sc = 0, 0
        self.grid = [[0 for i in range(len(self.data[0]))] for _ in self.data]
        for r, row in enumerate(self.data):
            for c, char in enumerate(row):
                self.grid[r][c] = self.data[r][c]
                if self.data[r][c] == "S":
                    sr, sc = r, c
        return sr, sc


class Part1Solution(Day21Solution):
    def result(self):
        ans = set()
        seen = set()
        R = len(self.data)
        C = len(self.data[0])
        sr, sc = self.parse_start()
        q = deque([(sr, sc, 0)])
        while q:
            r, c, d = q.popleft()
            if not ((0 <= r < R) and 0 <= c < C and self.grid[r][c] != "#"):
                continue
            if (r, c) in seen:
                continue
            seen.add((r, c))
            if d <= 64 and d % 2 == 0:
                ans.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                q.append((r + dr, c + dc, d + 1))
        return len(ans)


class Part2Solution(Day21Solution):
    def result(self):
        return None
