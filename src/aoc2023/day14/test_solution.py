from .solution import Part1Solution
from .solution import Part2Solution

example_input = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


def test_part1():
    result = Part1Solution(example_input).result()
    assert result == 136


def test_part2():
    result = Part2Solution(example_input).result()
    assert result == 64
