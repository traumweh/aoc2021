#!/usr/bin/env python3
import os, sys
import numpy as np

def init() -> tuple:
    os.chdir(os.path.dirname(sys.argv[0])) # change working dir

    with open("input", "r") as f:
        coords = list()
        folds = list()

        for line in f.readlines():
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

        return arr, folds

def tasks(data: tuple) -> tuple:
    (coords, folds) = data
    task1 = 0

    for i,fold in enumerate(folds):
        if fold[0] == "y":
            bottom_fold = coords[:fold[1]:-1]
            top_fold = coords[:fold[1]]

            top_fold[top_fold.shape[0] - bottom_fold.shape[0]:] += bottom_fold
            coords = top_fold
        else:
            left_fold = coords[:,:fold[1]:-1]
            right_fold = coords[:,:fold[1]]

            left_fold[:,left_fold.shape[1] - right_fold.shape[1]:] += right_fold
            coords = left_fold

        if i == 0:
            task1 = np.count_nonzero(coords)

    task2 = "\n\n"
    for line in coords:
        for c in line:
            task2 += "#" if c >= 1 else " "

        task2 += "\n"

    return (task1,task2)

print("1.) {}\t2.) {}".format(*tasks(init())))