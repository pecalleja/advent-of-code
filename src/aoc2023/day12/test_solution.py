from .solution import Part1Solution
from .solution import Part2Solution

example_input = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""


def test_part1():
    result = Part1Solution(example_input).result()
    assert result == 21


def test_part2():
    result = Part2Solution(example_input).result()
    assert result == 525152
