import re
from functools import reduce
from operator import itemgetter

from aoc2023 import Solution

NUMBER_RE = re.compile(r"\d+")


class Day5Solution(Solution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.raw_data = args[0]

    def result(self):
        raise NotImplementedError

    def parse(self):
        stanzas = self.raw_data.split("\n\n")
        return [int(m.group(0)) for m in NUMBER_RE.finditer(stanzas[0])], [
            sorted(
                (
                    (nums[1], nums[1] + nums[2], nums[0] - nums[1])
                    for line in stanza.splitlines()
                    if len(
                        nums := [
                            int(m.group(0)) for m in NUMBER_RE.finditer(line)
                        ]
                    )
                    == 3
                ),
                key=itemgetter(0),
            )
            for stanza in stanzas[1:]
        ]

    def remap(self, ranges, mappings):
        for start, end in ranges:
            for start2, end2, offset in mappings:
                if start2 >= end or start >= end2:
                    continue
                if start < start2:
                    yield start, start2
                    start = start2
                end2 = min(end, end2)
                yield start + offset, end2 + offset
                start = end2
            if start < end:
                yield start, end


class Part1Solution(Day5Solution):
    def result(self):
        seeds, mappings = self.parse()
        return min(
            map(
                itemgetter(0),
                reduce(self.remap, mappings, ((x, x + 1) for x in seeds)),
            )
        )


class Part2Solution(Day5Solution):
    def result(self):
        return None
