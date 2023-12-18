from aoc2023 import Solution


class Day18Solution(Solution):
    def result(self):
        raise NotImplementedError

    def solve(self, lines):
        x, y, a, l = 0, 0, 0, 0
        for d, n in lines:
            match d:
                case "0" | "R":
                    x += n
                    a += y * n
                case "1" | "D":
                    y += n
                case "2" | "L":
                    x -= n
                    a -= y * n
                case "3" | "U":
                    y -= n
            l += n
        return abs(a) + l // 2 + 1


class Part1Solution(Day18Solution):
    def result(self):
        return self.solve(
            (words[0], int(words[1]))
            for line in self.data
            if len(words := line.split()) >= 2
        )


class Part2Solution(Day18Solution):
    def result(self):
        return self.solve(
            (line[-2:-1], int(line[-7:-2], base=16))
            for line in self.data
            if line[-9:-7] == "(#" and line[-1:] == ")"
        )
