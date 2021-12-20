#!/usr/bin/env python3
import numpy as np
from scipy.ndimage import convolve

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            raw = f.read().split("\n\n")
            lines = raw[1].split("\n")

        self.__pad = 51 # steps + 1
        self.__conv = np.array([[1,2,4],[8,16,32],[64,128,256]])

        shape = len(lines) + 2 * self.__pad, len(lines[0]) + 2 * self.__pad
        self.data = np.zeros(shape, dtype=np.int0)
        self.algorithm = np.fromiter((1 if c == "#" else 0 for c in raw[0]), 
                    dtype=np.int0)

        for i,line in enumerate(lines, 1):
            self.data[i+self.__pad,self.__pad:-self.__pad] = \
                        [1 if c == "#" else 0 for c in list(line.strip())]

        self.__tasks()

    def __tasks(self) -> int:
        for i in range(1, self.__pad):
            tmp = convolve(self.data, self.__conv)

            for x in range(self.data.shape[0]):
                for y in range(self.data.shape[1]):
                    self.data[x,y] = self.algorithm[tmp[x,y]]

            if i == 2: self.task1 = np.sum(self.data)

        self.task2 = np.sum(self.data)

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))