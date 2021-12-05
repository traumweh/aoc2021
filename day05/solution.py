#!/usr/bin/env python3
import os, sys
import numpy as np

def init() -> np.array:
    # change working dir
    os.chdir(os.path.dirname(sys.argv[0]))

    # load and int-cast data
    with open("input", "r") as f:
        lines = f.readlines()
        data = np.empty((len(lines), 2, 2), dtype=np.int32)

        for i,line in enumerate(lines):
            data[i] = list(map(lambda x: x.split(","), line.split(" -> ")))

    return data

def task1(data: np.array) -> int:
    maximum = np.max(data) + 1
    overlaps = np.zeros((maximum, maximum), dtype=np.int32)

    for (x1,y1), (x2,y2) in data:
        if x1 == x2:
            overlaps[x1, min(y1,y2):max(y1,y2) + 1] += 1
        elif y1 == y2:
            overlaps[min(x1,x2):max(x1,x2) + 1, y1] += 1

    return len(overlaps[overlaps >= 2])

def task2(data: np.array) -> int:
    maximum = np.max(data) + 1
    overlaps = np.zeros((maximum, maximum), dtype=np.int32)

    for (x1,y1), (x2,y2) in data:
        xs = np.linspace(x1,x2,abs(x1-x2) + 1, dtype=np.int32)
        ys = np.linspace(y1,y2,abs(y1-y2) + 1, dtype=np.int32)
        overlaps[xs, ys] += 1

    return len(overlaps[overlaps >= 2])


data = init()
print(f"1.) {task1(data)}\t2.) {task2(data)}")