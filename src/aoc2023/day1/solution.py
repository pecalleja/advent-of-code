import re
from itertools import chain

from aoc2023 import Solution


class Part1Solution(Solution):
    def result(self):
        p = re.compile(r"\d")
        codes = [p.findall(x) for x in self.data]
        return sum([int(f"{x[0]}{x[-1]}") for x in codes])


class Part2Solution(Solution):
    digits = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    def result(self):
        codes = []
        number_pattern = re.compile(r"\d")
        for line in self.data:
            line_index = {}
            for i in range(len(self.digits)):
                digits_match = re.finditer(self.digits[i], line)
                number_match = re.finditer(number_pattern, line)
                for index in chain(digits_match, number_match):
                    line_index[index.start()] = index.group()
            line_index_keys = line_index.keys()
            first, last = min(line_index_keys), max(line_index_keys)
            for element in (first, last):
                if line_index[element] in self.digits:
                    line_index[element] = str(
                        self.digits.index(line_index[element])
                    )
            codes.append([line_index[first], line_index[last]])
        return sum([int(f"{x[0]}{x[-1]}") for x in codes])
