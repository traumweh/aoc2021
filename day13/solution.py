#!/usr/bin/env python3
import numpy as np

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            lines = f.readlines()

        coords = list()
        folds = list()

        for line in lines:
            line = line.strip()

            if line.startswith("fold"):
                fold = line.split("=")
                folds.append((fold[0][-1], int(fold[1])))
            elif line != "":
                coord = line.split(",")
                coords.append((int(coord[1]), int(coord[0])))

        arr = np.zeros((max(map(lambda x: x[0], coords)) + 1, 
                        max(map(lambda y: y[1], coords)) + 1))

        arr[tuple(list(zip(*coords)))] = 1

        self.coords = arr
        self.folds = folds
        self.__tasks()

    def __tasks(self) -> int:
        self.task1 = 0

        for i,fold in enumerate(self.folds):
            if fold[0] == "y":
                bottom_fold = self.coords[:fold[1]:-1]
                top_fold = self.coords[:fold[1]]

                top_fold[top_fold.shape[0] - bottom_fold.shape[0]:] += \
                            bottom_fold
                self.coords = top_fold
            else:
                left_fold = self.coords[:,:fold[1]:-1]
                right_fold = self.coords[:,:fold[1]]

                left_fold[:,left_fold.shape[1] - right_fold.shape[1]:] += \
                            right_fold
                self.coords = left_fold

            if i == 0:
                self.task1 = np.count_nonzero(self.coords)

        self.task2 = "\n\n"
        for line in self.coords:
            for c in line:
                self.task2 += "#" if c >= 1 else " "

            self.task2 += "\n"

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))