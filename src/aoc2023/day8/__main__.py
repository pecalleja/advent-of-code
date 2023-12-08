from .solution import Part1Solution
from .solution import Part2Solution


part1 = Part1Solution.from_file()
part2 = Part2Solution.from_file()
print(
    f"The result for day8 is part1: {part1.result()} , part2: {part2.result()}"
)
