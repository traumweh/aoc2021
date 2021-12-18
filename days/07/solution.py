#!/usr/bin/env python3
import numpy as np

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = np.array(f.readline().split(","), dtype=np.int64)

        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        min_fuel = (np.inf,np.inf)

        for i in range(np.min(self.data), np.max(self.data) + 1):
            # sum of distance between current position and new position
            fuel = np.sum(np.abs(i - self.data))

            if fuel < min_fuel[1]:
                min_fuel = (i, fuel)

        self.task1 = min_fuel[1]

    def __task2(self) -> int:
        min_fuel = (np.inf,np.inf)

        for i in range(np.min(self.data), np.max(self.data) + 1):
            dif = np.abs(i - self.data)

            # using the gauß sum formular (sum{0,...,n} = n(n+1)/2)
            fuel = np.sum(dif * (dif + 1) / 2, dtype=np.int64)

            if fuel < min_fuel[1]:
                min_fuel = (i, fuel)

        self.task2 = min_fuel[1]

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))