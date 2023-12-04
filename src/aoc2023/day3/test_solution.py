from .solution import Part1Solution
from .solution import Part2Solution

example_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def test_part1():
    result = Part1Solution(example_input).result()
    assert result == 4361


def test_part2():
    result = Part2Solution(example_input).result()
    assert result == 467835
