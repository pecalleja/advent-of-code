import re
from functools import reduce
from itertools import cycle
from math import lcm

from aoc2023 import Solution

NODE = re.compile(r"(\w+) = \((\w+), (\w+)\)")
INSTRUCTIONS = "LR"


class Day8Solution(Solution):
    network: dict = {}
    instructions: list

    def result(self):
        raise NotImplementedError

    def parse(self):
        self.instructions = list(map(INSTRUCTIONS.find, self.data[0]))
        for node in self.data[1:]:
            key, left, right = NODE.findall(node)[0]
            self.network[key] = [left, right]

    def step(self, node, instruction):
        return self.network[node][instruction]


class Part1Solution(Day8Solution):
    def result(self):
        self.parse()
        instructions = cycle(self.instructions)
        step = "AAA"
        count = 0
        while step != "ZZZ":
            instruction = next(instructions)
            step = self.step(step, instruction)
            count += 1
        return count


class Part2Solution(Day8Solution):
    def find_cycle(self, node: str):
        instructions = cycle(self.instructions)
        count = 0
        while not node.endswith("Z"):
            instruction = next(instructions)
            node = self.step(node, instruction)
            count += 1
        return count

    def result(self):
        self.parse()
        nodes = filter(lambda x: x.endswith("A"), self.network.keys())
        paths = list(map(self.find_cycle, nodes))
        return reduce(lcm, paths)
