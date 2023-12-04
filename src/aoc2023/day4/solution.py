from aoc2023 import Solution


class Day4Solution(Solution):
    def result(self):
        raise NotImplementedError

    def parse_cards(self):
        for line in self.data:
            _, card_numbers = line.split(":")
            card_numbers = card_numbers.strip()
            winning_numbers, your_numbers = card_numbers.split(" | ")
            winning_number = set(int(x) for x in winning_numbers.split())
            your_numbers = set(int(x) for x in your_numbers.split())
            yield len(winning_number & your_numbers)


class Part1Solution(Day4Solution):
    def result(self):
        return sum(1 << card >> 1 for card in self.parse_cards())


class Part2Solution(Day4Solution):
    def result(self):
        cards = list(self.parse_cards())
        counts = [1 for _ in cards]
        for i, card in enumerate(cards):
            for j in range(card):
                counts[i + j + 1] += counts[i]
        return sum(counts)
