#!/usr/bin/env python3
from functools import cache

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = list(map(lambda x: int(x[-2:]), f.read().split("\n")))

        self.__scores = [0,0]
        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        self.__pos = self.data.copy()
        self.__die = 1
        rolls = 0

        while True:
            rolls += 3
            if self.__task1_play(0): break
            rolls += 3
            if self.__task1_play(1): break

        self.task1 = min(self.__scores) * rolls

    def __task1_play(self, player: int) -> bool:
        roll = 3 * self.__die + 3
        self.__die += 3
        self.__pos[player] = (self.__pos[player] + roll - 1) % 10 + 1
        self.__scores[player] += self.__pos[player]
        return self.__scores[player] >= 1000

    def __task2(self) -> int:
        # list of pairs where a tuple's first element is the dice sum and the 
        # second element is the number of combinations to get that sum
        self.__throws = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]
        self.task2 = max(self.__task2_play(self.data[0], self.data[1], 0, 0))

    # caching makes this way faster, because there is no need to recalculate 
    # everything everytime. Speedup ca. x60
    @cache
    def __task2_play(self, p0: int, p1: int, s0: int, s1: int) -> list:
        if s1 >= 21: return [0,1]
        n = [0,0]

        for i,j in self.__throws:
            p0_new = (p0 + i - 1) % 10 + 1
            n_new = self.__task2_play(p1, p0_new, s1, s0 + p0_new)
            n = [n[0] + n_new[1] * j, n[1] + n_new[0] * j]

        return n

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))