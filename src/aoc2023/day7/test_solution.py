from .solution import Part1Solution
from .solution import Part2Solution

example_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


def test_part1():
    result = Part1Solution(example_input).result()
    assert result == 6440


def test_part2():
    result = Part2Solution(example_input).result()
    assert result == 5905
