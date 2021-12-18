#!/usr/bin/env python3
import numpy as np

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = np.asarray([list(line.strip()) for line in 
                    f.readlines()], dtype=np.float64)

        self.__tasks()

    def __tasks(self) -> tuple:
        self.task1 = i = 0
        self.task2 = -1

        while self.task2 == -1:
            i += 1
            self.data += 1

            while len(flashing := np.argwhere(self.data > 9)) > 0:
                for ix, iy in flashing:
                    (minx, maxx) = (max(0, ix-1), min(self.data.shape[0], ix+2))
                    (miny, maxy) = (max(0, iy-1), min(self.data.shape[1], iy+2))
                    self.data[minx:maxx,miny:maxy] += 1
                    self.data[ix,iy] = -np.inf

                    if i <= 100:
                        self.task1 += 1

            if self.data[self.data == -np.inf].size == self.data.size:
                self.task2 = i

            self.data[self.data == -np.inf] = 0

        return self.task1, self.task2

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))