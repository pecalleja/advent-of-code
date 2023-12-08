import re
from itertools import cycle

from aoc2023 import Solution

LETTERS = re.compile(r"[A-Z]{3}")
INSTRUCTIONS = "LR"


class Day8Solution(Solution):
    network: dict = {}
    instructions: iter

    def result(self):
        raise NotImplementedError

    def parse(self):
        self.instructions = cycle(map(INSTRUCTIONS.find, self.data[0]))
        for node in self.data[1:]:
            key, left, right = LETTERS.findall(node)
            self.network[key] = [left, right]


class Part1Solution(Day8Solution):
    def result(self):
        self.parse()
        step = "AAA"
        count = 0
        while step != "ZZZ":
            instruction = next(self.instructions)
            step = self.network[step][instruction]
            count += 1
        return count


class Part2Solution(Day8Solution):
    def result(self):
        return None
