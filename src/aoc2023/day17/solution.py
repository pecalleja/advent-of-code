from aoc2023 import Solution
import heapq
from enum import IntEnum


class _Direction(IntEnum):
    U = 0
    L = 1
    D = 2
    R = 3

    def __add__(self, other):
        return _Direction((self.value + other) % len(_Direction))

    def __sub__(self, other):
        return _Direction((self.value - other) % len(_Direction))


class Day17Solution(Solution):

    def result(self):
        raise NotImplementedError

    def solve(self, ok, turns):
        data = [[int(char) for char in line] for line in self.data if line]
        queue = [(0, (0, 0, _Direction.R, 0))]
        best = {(0, 0, _Direction.R, 0): 0}
        while queue:
            cost, state = heapq.heappop(queue)
            y1, x1, direction1, distance1 = state
            if y1 == len(data) - 1 and x1 == len(data[-1]) - 1 and ok(distance1):
                return cost
            if cost > best[state]:
                continue
            for direction2 in turns(direction1, distance1):
                y2, x2 = y1, x1
                match direction2:
                    case _Direction.U:
                        y2 -= 1
                    case _Direction.L:
                        x2 -= 1
                    case _Direction.D:
                        y2 += 1
                    case _Direction.R:
                        x2 += 1
                if not (0 <= y2 < len(data) and 0 <= x2 < len(data[y2])):
                    continue
                cost2 = cost + data[y2][x2]
                distance2 = distance1 + 1 if direction1 == direction2 else 1
                state2 = (y2, x2, direction2, distance2)
                if state2 in best and best[state2] <= cost2:
                    continue
                best[state2] = cost2
                heapq.heappush(queue, (cost2, state2))
        return None


class Part1Solution(Day17Solution):

    def turns(self, direction, distance):
        turns = [direction - 1, direction + 1]
        if distance < 3:
            turns.append(direction)
        return turns

    def result(self):
        return self.solve(lambda x: True, self.turns)


class Part2Solution(Day17Solution):

    def turns(self, direction, distance):
        turns = []
        if distance >= 4:
            turns.extend([direction - 1, direction + 1])
        if distance < 10:
            turns.append(direction)
        return turns

    def result(self):
        return self.solve(lambda x: x >= 4, self.turns)
