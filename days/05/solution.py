#!/usr/bin/env python3
import numpy as np

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            lines = f.readlines()

        self.data = np.empty((len(lines), 2, 2), dtype=np.int32)

        for i,line in enumerate(lines):
            self.data[i] = list(map(lambda x: x.split(","),
                    line.split(" -> ")))

        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        maximum = np.max(self.data) + 1
        overlaps = np.zeros((maximum, maximum), dtype=np.int32)

        for (x1,y1), (x2,y2) in self.data:
            if x1 == x2:
                overlaps[x1, min(y1,y2):max(y1,y2) + 1] += 1
            elif y1 == y2:
                overlaps[min(x1,x2):max(x1,x2) + 1, y1] += 1

        self.task1 = len(overlaps[overlaps >= 2])

    def __task2(self) -> int:
        maximum = np.max(self.data) + 1
        overlaps = np.zeros((maximum, maximum), dtype=np.int32)

        for (x1,y1), (x2,y2) in self.data:
            xs = np.linspace(x1,x2,abs(x1-x2) + 1, dtype=np.int32)
            ys = np.linspace(y1,y2,abs(y1-y2) + 1, dtype=np.int32)
            overlaps[xs, ys] += 1

        self.task2 = len(overlaps[overlaps >= 2])

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))