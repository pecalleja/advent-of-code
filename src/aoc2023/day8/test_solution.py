from .solution import Part1Solution
from .solution import Part2Solution


def test_part1_example1():
    example_input = """
    RL

    AAA = (BBB, CCC)
    BBB = (DDD, EEE)
    CCC = (ZZZ, GGG)
    DDD = (DDD, DDD)
    EEE = (EEE, EEE)
    GGG = (GGG, GGG)
    ZZZ = (ZZZ, ZZZ)
    """
    result = Part1Solution(example_input).result()
    assert result == 2


def test_part1_example2():
    example_input = """
    LLR

    AAA = (BBB, BBB)
    BBB = (AAA, ZZZ)
    ZZZ = (ZZZ, ZZZ)
    """
    result = Part1Solution(example_input).result()
    assert result == 6


def test_part2():
    example_input = ""
    result = Part2Solution(example_input).result()
    assert result is None
