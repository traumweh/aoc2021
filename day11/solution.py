#!/usr/bin/env python3
import os, sys
import numpy as np

def init() -> list:
    os.chdir(os.path.dirname(sys.argv[0])) # change working dir

    with open("input", "r") as f:
        return np.asarray([list(line.strip()) for line in f.readlines()], dtype=np.float64)

def tasks(data: list) -> tuple:
    task1 = i = 0
    task2 = -1

    while task2 == -1:
        i += 1
        data += 1

        while len(flashing := np.argwhere(data > 9)) > 0:
            for ix, iy in flashing:
                (minx, maxx) = (max(0, ix-1), min(data.shape[0], ix+2))
                (miny, maxy) = (max(0, iy-1), min(data.shape[1], iy+2))
                data[minx:maxx,miny:maxy] += 1
                data[ix,iy] = -np.inf

                if i <= 100:
                    task1 += 1

        if data[data == -np.inf].size == data.size:
            task2 = i

        data[data == -np.inf] = 0

    return task1, task2


print("1.) {}\t2.) {}".format(*tasks(init())))