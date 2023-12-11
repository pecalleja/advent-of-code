from .solution import Part1Solution
from .solution import Part2Solution


def test_part1():
    example_input = """
    .....
    .S-7.
    .|.|.
    .L-J.
    .....
    """
    result = Part1Solution(example_input).result()
    assert result == 4


def test_part2():
    example_input = """
    FF7FSF7F7F7F7F7F---7
    L|LJ||||||||||||F--J
    FL-7LJLJ||||||LJL-77
    F--JF--7||LJLJIF7FJ-
    L---JF-JLJIIIIFJLJJ7
    |F|F-JF---7IIIL7L|7|
    |FFJF7L7F-JF7IIL---7
    7-L-JL7||F7|L7F-7F7|
    L.L7LFJ|||||FJL7||LJ
    L7JLJL-JLJLJL--JLJ.L
    """
    result = Part2Solution(example_input).result()
    assert result == 10
