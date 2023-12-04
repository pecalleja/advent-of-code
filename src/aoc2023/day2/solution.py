import os
import re


class Solution:
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    def __init__(self, data_input):
        self.data = data_input

    def result(self):
        pattern = re.compile(r"\d+\sred|\d+\sgreen|\d+\sblue")
        result = 0
        for line in self.data:
            game_id, game_result = line.split(":")
            game_id = game_id.split()[-1]
            game_id = int(game_id)
            game_result = game_result.strip()
            values = {
                "red": [],
                "green": [],
                "blue": [],
            }
            for match in pattern.findall(game_result):
                value, color = match.split()
                values[color].append(int(value))
            multiplication = 1
            for color, elements in values.items():
                values[color] = max(elements)
                multiplication *= values[color]
            print(f"game {game_id} values: {values}")
            result += multiplication
        return result


if __name__ == "__main__":
    this_dir = os.path.dirname(__file__)
    full_path = os.path.join(this_dir, "input.txt")
    with open(full_path) as file_input:
        data = file_input.readlines()
        result = Solution(data).result()
        print(f"The result for input.txt is: {result}")
