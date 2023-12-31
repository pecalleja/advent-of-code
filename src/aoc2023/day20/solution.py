from collections import defaultdict
from collections import deque
from functools import reduce
from math import lcm

from aoc2023 import Solution


class _Bool:
    __slots__ = ("value",)

    def __init__(self, value=False):
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)

    def __bool__(self):
        return bool(self.value)


class Day20Solution(Solution):
    def result(self):
        raise NotImplementedError

    def parse(self):
        machines, dependencies = {}, defaultdict(set)
        for line in self.data:
            if " -> " not in line:
                continue
            lhs, rhs = line.split(" -> ", maxsplit=1)
            rhs = rhs.split(", ")
            if lhs.startswith("%"):
                machines[lhs[1:]] = _Bool(), rhs
            elif lhs.startswith("&"):
                machines[lhs[1:]] = {}, rhs
            else:
                machines[lhs] = None, rhs
        for key, value in machines.items():
            _, dsts = value
            for dst in dsts:
                dependencies[dst].add(key)
                if dst in machines and isinstance(machines[dst][0], dict):
                    machines[dst][0][key] = False
        return machines, dependencies


class Part1Solution(Day20Solution):
    def result(self):
        machines, _ = self.parse()
        x, y = 0, 0
        for _ in range(1000):
            queue = deque([("button", "broadcaster", False)])
            while queue:
                src, key, value = queue.popleft()
                if value:
                    x += 1
                else:
                    y += 1
                target, dsts = machines.get(key, (None, ()))
                match target:
                    case _Bool():
                        if value:
                            continue
                        value = target.value = not target
                    case dict():
                        target[src] = value
                        value = not all(target.values())
                queue.extend((key, dst, value) for dst in dsts)
        return x * y


def _bfs(dependencies, dst):
    visited, stack = set(), [dst]
    while stack:
        dst = stack.pop()
        if dst in visited:
            continue
        visited.add(dst)
        stack.extend(dependencies.get(dst, ()))
    return visited


def _loop(machines, dst):
    seen = {}
    for _ in range(5000):
        snapshot = tuple(
            (
                key,
                not all(target.values())
                if isinstance(target, dict)
                else bool(target),
            )
            for key, (target, _) in machines.items()
            if target is not None
        )
        if snapshot in seen:
            break
        seen[snapshot] = len(seen)
        queue = deque([("button", "broadcaster", False)])
        while queue:
            src, key, value = queue.popleft()
            if key == dst:
                pass
            target, dsts = machines.get(key, (None, ()))
            match target:
                case _Bool():
                    if value:
                        continue
                    value = target.value = not target
                case dict():
                    target[src] = value
                    value = not all(target.values())
            queue.extend((key, dst, value) for dst in dsts)
    else:
        raise RuntimeError("ran out of iterations")
    if seen[snapshot] != 1:
        raise NotImplementedError()
    return len(seen) - 1


class Part2Solution(Day20Solution):
    def result(self):
        machines, dependencies = self.parse()
        if machines.get("broadcast", (None,))[0] is not None:
            raise NotImplementedError()
        (conjunction,) = dependencies["rx"]
        if not isinstance(machines[conjunction][0], dict):
            raise NotImplementedError()
        subsets = {
            dst: _bfs(dependencies, dst) for dst in dependencies[conjunction]
        }
        if any(
            s1 is not s2 and s1 & s2 != set(("broadcaster",))
            for s1 in subsets.values()
            for s2 in subsets.values()
        ):
            raise NotImplementedError()
        return reduce(
            lcm,
            (
                _loop(
                    {
                        key: value
                        for key, value in machines.items()
                        if key in subset
                    },
                    dst,
                )
                for dst, subset in subsets.items()
            ),
            1,
        )
