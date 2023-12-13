from .solution import Part1Solution
from .solution import Part2Solution

example_input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""


def test_part1():
    result = Part1Solution(example_input).result()
    assert result == 405


def test_part2():
    result = Part2Solution(example_input).result()
    assert result == 400
