from .solution import Part1Solution
from .solution import Part2Solution

example_input = """
Time:      7  15   30
Distance:  9  40  200
"""


def test_part1():
    result = Part1Solution(example_input).result()
    assert result == 288


def test_part2():
    result = Part2Solution(example_input).result()
    assert result == 71503
