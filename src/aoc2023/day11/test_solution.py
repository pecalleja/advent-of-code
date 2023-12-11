import pytest

from .solution import Day11Solution

example_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""


@pytest.mark.parametrize("factor, output", [(2, 374), (10, 1030), (100, 8410)])
def test_solution(factor, output):
    part = Day11Solution(factor=factor, data=example_input)
    part.factor = factor
    result = part.result()
    assert result == output
