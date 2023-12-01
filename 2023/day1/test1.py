from .part1 import Solution


def test_part1():
    example_input = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    result = Solution(example_input).result()
    assert result == 142
