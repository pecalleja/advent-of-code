from aoc2023 import Solution


class Day4Solution(Solution):
    def result(self):
        raise NotImplementedError

    def parsed_card(self):
        for line in self.data:
            card_id, card_numbers = line.split(":")
            card_id = card_id.split()[-1]
            card_id = int(card_id)
            card_numbers = card_numbers.strip()
            winning_numbers, your_numbers = card_numbers.split(" | ")
            winning_number = [int(x) for x in winning_numbers.split()]
            your_numbers = [int(x) for x in your_numbers.split()]
            yield card_id, winning_number, your_numbers


class Part1Solution(Day4Solution):
    def result(self):
        result = 0
        for card_id, winning, your in self.parsed_card():
            won = 0
            for number in your:
                if number in winning:
                    if won < 2:
                        won += 1
                    else:
                        won = won * 2
            result += won
        return result


class Part2Solution(Day4Solution):
    def result(self):
        return None
