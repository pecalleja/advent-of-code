from .solution import Solution


def test_part():
    example_input = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    s = Solution(example_input)
    numbers, symbols = s.parse()
    assert s.part1(numbers, symbols) == 4361
