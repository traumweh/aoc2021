#!/usr/bin/env python3
import os, sys
import numpy as np

def init() -> list:
    # change working dir
    os.chdir(os.path.dirname(sys.argv[0]))

    # load and int-cast data
    with open("input", "r") as f:
        data = np.array([np.array(l).astype(np.int32) for l in [list(line.strip()) for line in f.readlines()]])

    return data

def task1(data: list) -> int:
    # count number of zeros / ones per column
    n_zeros = np.zeros((data.shape[1])) + np.sum(data, axis=0)
    n_ones = np.zeros((data.shape[1])) + np.abs(np.sum(1 - data, axis=0))

    # connect to single array
    stack = np.column_stack((n_zeros, n_ones))
    gamma = 0
    epsilon = 0
    length = stack.shape[0]

    # for each column check if more zeros or ones
    for i in range(0, length):
        if np.argmax(stack[i]) == 0:
            epsilon += 2 ** (length - 1 - i)
        else:
            gamma += 2 ** (length - 1 - i)

    # return power consumption
    return gamma * epsilon

def task2(data: list) -> int:
    def calc(data: list, negate: bool) -> int:
        copy = data.copy()
        i = 0

        while len(copy) > 1:
            ones = np.sum(copy, axis=0)
            zeros = np.abs(np.sum(1 - copy, axis=0))

            check = ones[i] >= zeros[i]
            if (check if not negate else not check):
                copy = copy[copy[:,i] != 1]
            else:
                copy = copy[copy[:,i] != 0]

            i += 1
        
        c = 0
        for bit in copy[0]:
            c = (c << 1) | bit

        return c

    # negate = True     ->  most common; ones >= zeros
    # negate = False    ->  least common; ones < zeros
    return calc(data, False) * calc(data, True)


data = init()
print(f"1.) {task1(data)}\t2.) {task2(data)}")