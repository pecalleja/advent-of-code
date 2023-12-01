import os
import re
from itertools import chain


class Solution:
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

    def __init__(self, input_data):
        self.input_data = input_data

    def result(self):
        codes = []
        number_pattern = re.compile(r"\d")
        for line in self.input_data:
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


if __name__ == "__main__":
    this_dir = os.path.dirname(__file__)
    full_path = os.path.join(this_dir, "input.txt")
    with open(full_path) as file_input:
        data = file_input.readlines()
        result = Solution(data).result()
        print(f"The result for input.txt is: {result}")
