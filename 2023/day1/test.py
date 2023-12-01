from .solution import Solution


def test_part1():
    example_input = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    result = Solution(example_input).result()
    assert result == 142


def test_part2():
    example_input = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    result = Solution(example_input).result()
    assert result == 281
