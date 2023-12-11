from enum import Enum

from aoc2023 import Solution


class Direction(Enum):
    """
    Cardinal direction.
    """

    U = "up"
    L = "left"
    D = "down"
    R = "right"

    def move(self, pos):
        """
        Move a point by one step in this direction.
        """
        y, x = pos
        match self:
            case Direction.U:
                return y - 1, x
            case Direction.L:
                return y, x - 1
            case Direction.D:
                return y + 1, x
            case Direction.R:
                return y, x + 1

    def __neg__(self):
        match self:
            case Direction.U:
                return Direction.D
            case Direction.L:
                return Direction.R
            case Direction.D:
                return Direction.U
            case Direction.R:
                return Direction.L


_SYMBOLS = {
    "|": (Direction.U, Direction.D),
    "-": (Direction.L, Direction.R),
    "L": (Direction.U, Direction.R),
    "J": (Direction.U, Direction.L),
    "7": (Direction.L, Direction.D),
    "F": (Direction.D, Direction.R),
}


class Day10Solution(Solution):
    def result(self):
        raise NotImplementedError

    def _part1(self):
        for y, line in enumerate(self.data):
            for x, char in enumerate(line):
                if char != "S":
                    continue
                start_pos = y, x
                for start_dir in Direction:
                    pos = start_dir.move(start_pos)
                    last_dir = -start_dir
                    path = [start_pos]
                    while pos != start_pos:
                        y, x = pos
                        try:
                            char = self.data[y][x]
                        except IndexError:
                            break
                        dirs = _SYMBOLS.get(char, ())
                        if last_dir not in dirs:
                            break
                        path.append(pos)
                        (next_dir,) = (d for d in dirs if d != last_dir)
                        pos = next_dir.move(pos)
                        last_dir = -next_dir
                    else:
                        return start_pos, (start_dir, last_dir), path


class Part1Solution(Day10Solution):
    def result(self):
        return len(self._part1()[2]) // 2


class Part2Solution(Day10Solution):
    def result(self):
        start_pos, start_dirs, path = self._part1()
        path = sorted(path)
        count, up, down, path_index = 0, False, False, 0
        for y, line in enumerate(self.data):
            for x, char in enumerate(line):
                if path_index < len(path) and path[path_index] == (y, x):
                    dirs = (
                        start_dirs if start_pos == (y, x) else _SYMBOLS[char]
                    )
                    path_index += 1
                    up ^= Direction.U in dirs
                    down ^= Direction.D in dirs
                else:
                    if up and down:
                        count += 1
                    assert up == down
        return count
