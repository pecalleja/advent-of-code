import multiprocessing
from enum import Enum
from itertools import chain

from aoc2023 import Solution


class _Direction(Enum):
    U = "up"
    L = "left"
    D = "down"
    R = "right"


_LUT = {
    (_Direction.U, "/"): (_Direction.R,),
    (_Direction.U, "\\"): (_Direction.L,),
    (_Direction.U, "-"): (_Direction.L, _Direction.R),
    (_Direction.L, "/"): (_Direction.D,),
    (_Direction.L, "\\"): (_Direction.U,),
    (_Direction.L, "|"): (_Direction.D, _Direction.U),
    (_Direction.D, "/"): (_Direction.L,),
    (_Direction.D, "\\"): (_Direction.R,),
    (_Direction.D, "-"): (_Direction.L, _Direction.R),
    (_Direction.R, "/"): (_Direction.U,),
    (_Direction.R, "\\"): (_Direction.D,),
    (_Direction.R, "|"): (_Direction.D, _Direction.U),
}


def _move(y, x, d):
    match d:
        case _Direction.U:
            return y - 1, x
        case _Direction.L:
            return y, x - 1
        case _Direction.D:
            return y + 1, x
        case _Direction.R:
            return y, x + 1


class Day16Solution(Solution):
    def result(self):
        raise NotImplementedError

    def fill(self, data, y, x, d):
        stack = [(y, x, d)]
        visited = set(stack)
        while stack:
            y1, x1, d1 = stack.pop()
            for d2 in _LUT.get((d1, data[y1][x1]), (d1,)):
                y2, x2 = _move(y1, x1, d2)
                if (
                    0 <= y2 < len(data)
                    and 0 <= x2 < len(data[y2])
                    and (y2, x2, d2) not in visited
                ):
                    stack.append((y2, x2, d2))
                    visited.add((y2, x2, d2))
        return len({(y, x) for y, x, _ in visited})


class Part1Solution(Day16Solution):
    def result(self):
        return self.fill(list(filter(None, self.data)), 0, 0, _Direction.R)


class Part2Solution(Day16Solution):
    DATA2 = []

    def result(self):
        with multiprocessing.Pool(
            initializer=self._initializer2, initargs=(self.data,)
        ) as p:
            return max(
                p.imap_unordered(
                    self._fill2,
                    chain(
                        ((y, 0, _Direction.R) for y in range(len(self.data))),
                        (
                            (0, x, _Direction.D)
                            for x in range(len(self.data[0]))
                        ),
                        (
                            (y, len(self.data[0]) - 1, _Direction.L)
                            for y in range(len(self.data))
                        ),
                        (
                            (len(self.data) - 1, x, _Direction.U)
                            for x in range(len(self.data[-1]))
                        ),
                    ),
                )
            )

    def _initializer2(self, data):
        self.DATA2[:] = data

    def _fill2(self, args):
        y, x, d = args
        return self.fill(self.DATA2, y, x, d)
