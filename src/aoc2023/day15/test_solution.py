from .solution import Part1Solution
from .solution import Part2Solution

example_input = "HASH"


def test_part1():
    result = Part1Solution(example_input).result()
    assert result == 52


def test_part2():
    result = Part2Solution(example_input).result()
    assert result is None
