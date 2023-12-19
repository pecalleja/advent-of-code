from math import prod

from aoc2023 import Solution


class Day19Solution(Solution):
    def __init__(self, data):
        self.rules, self.points = data.split("\n\n", maxsplit=1)
        super().__init__(data)

    def result(self):
        raise NotImplementedError

    def parse_rules(self):
        for line in self.rules.splitlines():
            if "{" not in line or not line.endswith("}"):
                continue
            yield line[: line.index("{")], [
                (
                    rule[rule.index(":") + 1 :],
                    (rule[0], rule[1], int(rule[2 : rule.index(":")])),
                )
                if ":" in rule
                else (rule, None)
                for rule in line[line.index("{") + 1 : -1].split(",")
            ]

    def parse_points(self):
        for line in self.points.splitlines():
            if not line.startswith("{") or not line.endswith("}"):
                continue
            yield {
                kv[0]: int(kv[2:])
                for kv in line[1:-1].split(",")
                if kv[1] == "="
            }


class Part1Solution(Day19Solution):
    def result(self):
        rules = dict(self.parse_rules())
        points = list(self.parse_points())

        acc = 0
        for point in points:
            name = "in"
            while name in rules:
                for name, comparison in rules[name]:
                    if not comparison:
                        break
                    key, compare, value = comparison
                    if (
                        compare == "<"
                        and point[key] < value
                        or compare == ">"
                        and point[key] > value
                    ):
                        break
                else:
                    raise RuntimeError("unreachable")
            if name == "A":
                acc += sum(point.values())
        return acc


class Part2Solution(Day19Solution):
    def result(self):
        rules = dict(self.parse_rules())

        def go(name, bounds):
            if any(first > last for first, last in bounds.values()):
                return 0
            if name == "A":
                return prod(
                    last - first + 1 for first, last in bounds.values()
                )
            if name not in rules:
                return 0
            acc = 0
            # pylint: disable=R1704
            for name, comparison in rules[name]:
                if not comparison:
                    acc += go(name, bounds)
                    break
                key, compare, value = comparison
                lo, hi = bounds[key]
                match compare:
                    case "<":
                        intersection = lo, min(hi, value - 1)
                        difference = value, hi
                    case ">":
                        intersection = max(lo, value + 1), hi
                        difference = lo, min(hi, value)
                    case _:
                        raise KeyError(compare)
                if difference[0] > difference[1]:
                    break
                acc += go(name, bounds | {key: intersection})
                bounds[key] = difference
            return acc

        return go("in", {k: (1, 4000) for k in "xmas"})
