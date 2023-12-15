from aoc2023 import Solution


class Day15Solution(Solution):
    def __init__(self, data, *args, **kwargs):
        self.data = [x.strip() for x in data.split(",") if x.strip()]

    def result(self):
        raise NotImplementedError


class Part1Solution(Day15Solution):
    def result(self):
        result = 0
        for string in self.data:
            hash_result = 0
            for c in string:
                hash_result += ord(c)
                hash_result *= 17
                hash_result %= 256
            result += hash_result
        return result


class Part2Solution(Day15Solution):
    def result(self):
        return None
