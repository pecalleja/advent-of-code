import os
import re


class Solution:
    def __init__(self, input_data):
        self.input_data = input_data

    def result(self):
        p = re.compile(r"\d")
        codes = [p.findall(x) for x in self.input_data]
        return sum([int(f"{x[0]}{x[-1]}") for x in codes])


if __name__ == "__main__":
    this_dir = os.path.dirname(__file__)
    full_path = os.path.join(this_dir, "input.txt")
    with open(full_path) as file_input:
        data = file_input.readlines()
        result = Solution(data).result()
        print(f"The result for input.txt is: {result}")
