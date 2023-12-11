from .solution import Day11Solution


part1 = Day11Solution.from_file(factor=2)
part2 = Day11Solution.from_file(factor=1000000)
print(
    f"The result for day11 is part1: {part1.result()} ,part2: {part2.result()}"
)
