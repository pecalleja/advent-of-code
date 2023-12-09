from aoc2023 import Solution


class Day9Solution(Solution):

    def result(self):
        raise NotImplementedError

    def _extrapolate(self, nums):
        c, s, n = 1, 0, len(nums)
        for i, x in enumerate(nums):
            c, s = c * (n - i) // (i + 1), c * x - s
        return s


class Part1Solution(Day9Solution):
    def result(self):
        return sum(
            self._extrapolate([int(word) for word in line.split() if word])
            for line in self.data
        )


class Part2Solution(Day9Solution):
    def result(self):
        return sum(
            self._extrapolate([int(word) for word in line.split() if word][::-1])
            for line in self.data
        )
