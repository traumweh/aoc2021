#!/usr/bin/env python3
import numpy as np

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = np.array(f.readline().split(","), dtype=np.uint8)

        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        self.task1 = self.__simulate_population(80)

    def __task2(self) -> int:
        self.task2 = self.__simulate_population(256)

    def __simulate_population(self, n_iterations: int) -> int:
        # create lanternfish array which holds 9 values.
        # each value e is the amount of lanternfishes who need idx_of(e) 
        # days (iterations) until they spawn a new lanternfish
        lfs = np.zeros((9,), dtype=np.uint64)

        # initialise lfs with the input data
        for d in self.data:
            lfs[d] += 1

        # run all n iterations
        for _ in range(1, n_iterations + 1):
            # lanternfish spawning a lanternfish today take 6 days for the next.
            # Using index 7 because the days haven't been decremented yet
            lfs[7] += lfs[0]

            # rolling the array to decrement the days (time until next spawn)
            # also produces lfs[8] <- lfs[0], thereby creating new lanternfish
            lfs = np.roll(lfs, -1)

        # return total number of lanternfish after n interations
        return np.sum(lfs)

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))