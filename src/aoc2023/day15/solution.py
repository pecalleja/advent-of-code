from functools import reduce

from aoc2023 import Solution


class Day15Solution(Solution):
    def __init__(self, data, *args, **kwargs):
        self.data = [x.strip() for x in data.split(",") if x.strip()]

    def result(self):
        raise NotImplementedError

    def hash(self, string):
        return reduce(lambda acc, c: 17 * (acc + ord(c)) % 256, string, 0)


class Part1Solution(Day15Solution):
    def result(self):
        return sum(map(self.hash, self.data))


class Part2Solution(Day15Solution):
    def result(self):
        buckets = [{} for _ in range(256)]
        for step in self.data:
            if step.endswith("-"):
                key = step[:-1]
                buckets[self.hash(key)].pop(key, None)
            elif "=" in step:
                key = step[: step.index("=")]
                buckets[self.hash(key)][key] = int(step[step.index("=") + 1 :])
        return sum(
            (i + 1) * sum((j + 1) * n for j, n in enumerate(bucket.values()))
            for i, bucket in enumerate(buckets)
        )
