from .solution import Part1Solution
from .solution import Part2Solution

example_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def test_part1_example1():

    result = Part1Solution(example_input).result()
    assert result == 114


def test_part2():
    result = Part2Solution(example_input).result()
    assert result == 2
