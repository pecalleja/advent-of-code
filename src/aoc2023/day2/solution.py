import re
from functools import reduce

from aoc2023 import Solution


class Day2Solution(Solution):
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    def result(self):
        raise NotImplementedError

    def parsed_game(self):
        pattern = re.compile(r"\d+\sred|\d+\sgreen|\d+\sblue")
        for line in self.data:
            game_id, game_result = line.split(":")
            game_id = game_id.split()[-1]
            game_id = int(game_id)
            game_result = game_result.strip()
            for match in pattern.findall(game_result):
                value, color = match.split()
                yield game_id, color, int(value)


class Part1Solution(Day2Solution):
    def result(self):
        games = {i: True for i in range(1, len(self.data) + 1)}
        for game_id, color, value in self.parsed_game():
            if self.limits[color] < value:
                games[game_id] = False
        result = sum(
            [game_id for game_id, valid in games.items() if valid is True]
        )
        return result


class Part2Solution(Day2Solution):
    def result(self):
        games = {
            i: {
                "red": [],
                "green": [],
                "blue": [],
            }
            for i in range(1, len(self.data) + 1)
        }
        for game_id, color, value in self.parsed_game():
            games[game_id][color].append(value)
        result = 0
        for game_id, values in games.items():
            for color, elements in values.items():
                values[color] = max(elements)
            multiplication = reduce(lambda x, y: x * y, values.values())
            result += multiplication
        return result
