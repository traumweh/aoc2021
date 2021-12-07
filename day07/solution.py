#!/usr/bin/env python3
import os, sys
import numpy as np

def init() -> np.array:
    # change working dir
    os.chdir(os.path.dirname(sys.argv[0]))

    # load and int-cast data
    with open("input", "r") as f:
        data = np.array(f.readline().split(","), dtype=np.int64)

    return data

def task1(data: np.array) -> tuple[int]:
    min_fuel = (np.inf,np.inf)

    for i in range(np.min(data), np.max(data) + 1):
        # sum of distance between current position and new position
        fuel = np.sum(np.abs(i - data))

        if fuel < min_fuel[1]:
            min_fuel = (i, fuel)

    return min_fuel

def task2(data: np.array) -> tuple[int]:
    min_fuel = (np.inf,np.inf)

    for i in range(np.min(data), np.max(data) + 1):
        dif = np.abs(i - data)

        # using the gauß sum formular (sum{0,...,n} = n(n+1)/2)
        fuel = np.sum(dif * (dif + 1) / 2, dtype=np.int64)

        if fuel < min_fuel[1]:
            min_fuel = (i, fuel)

    return min_fuel


data = init()
(pos1, fuel1), (pos2, fuel2) = (task1(data), task2(data))
print(f"1.) Pos: {pos1:>5};\tFuel: {fuel1:>10}\n"\
        f"2.) Pos: {pos2:>5};\tFuel: {fuel2:>10}")