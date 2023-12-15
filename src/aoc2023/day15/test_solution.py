from .solution import Part1Solution
from .solution import Part2Solution


def test_part1_1():
    example_input = "HASH"
    result = Part1Solution(example_input).result()
    assert result == 52


def test_part1_2():
    example_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    result = Part1Solution(example_input).result()
    assert result == 1320


def test_part2():
    example_input = ""
    result = Part2Solution(example_input).result()
    assert result is None
