#!/usr/bin/env python3
import os, sys
import numpy as np

def init() -> np.array:
    # change working dir
    os.chdir(os.path.dirname(sys.argv[0]))

    # load and int-cast data
    with open("input", "r") as f:
        data = np.array(f.readline().split(","), dtype=np.uint8)

    return data

def task1(data: np.array) -> int:
    return simulate_population(data, 80)

def task2(data: np.array) -> int:
    return simulate_population(data, 256)

def simulate_population(data: np.array, n_iterations: int) -> int:
    # create lanternfish array which holds 9 values.
    # each value e is the amount of lanternfishes who need idx_of(e) 
    # days (iterations) until they spawn a new lanternfish
    lfs = np.zeros((9,), dtype=np.uint256)

    # initialise lfs with the input data
    for d in data:
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

data = init()
print(f"1.) {task1(data)}\t2.) {task2(data)}")