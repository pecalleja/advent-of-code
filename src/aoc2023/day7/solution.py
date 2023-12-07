from collections import Counter

from aoc2023 import Solution


class Day7Solution(Solution):
    cards: str

    def result(self):
        raise NotImplementedError

    def parse(self):
        for line in self.data:
            hand, bid = line.split()
            yield hand, int(bid)

    def rank(self, hand: tuple[int]):
        counts = Counter(x for x in hand if x >= 0).most_common(2)
        count0 = counts[0][1] if counts else 0
        count1 = counts[1][1] if len(counts) > 1 else 0
        jokers = sum(x < 0 for x in hand)
        if count0 + jokers >= 5:
            return 6
        if count0 + jokers >= 4:
            return 5
        if count0 + count1 + jokers >= 5:
            return 4
        if count0 + jokers >= 3:
            return 3
        if count0 + count1 + jokers >= 4:
            return 2
        if count0 + jokers >= 2:
            return 1
        return 0

    def solve(self):
        ranked_hands = []
        for hand, bid in self.parse():
            hand_map = tuple(map(self.cards.find, hand))
            hand_rank = self.rank(hand_map)
            ranked_hands.append((hand_rank, hand_map, bid))
        result = 0
        for rank_pos, (_, _, bid) in enumerate(sorted(ranked_hands)):
            result += (rank_pos + 1) * bid
        return result


class Part1Solution(Day7Solution):
    cards = "23456789TJQKA"

    def result(self):
        return self.solve()


class Part2Solution(Day7Solution):
    cards = "23456789TQKA"

    def result(self):
        return self.solve()
