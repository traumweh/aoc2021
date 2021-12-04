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
    gamma_bits = np.round(np.mean(data, axis=0)).astype(np.int32)
    gamma = bitarr_to_int(gamma_bits)
    epsilon = bitarr_to_int(1 - gamma_bits)

    # return power consumption
    return gamma * epsilon

def task2(data: list) -> int:
    def calc(data: list, oxygen: bool) -> int:
        copy = data.copy()
        i = 0

        while len(copy) > 1:
            zeros = np.sum(1 - copy[:,i], axis=0)
            ones = np.sum(copy[:,i], axis=0)
            most_common_bit = 1 if ones >= zeros else 0

            if oxygen:
                copy = copy[copy[:,i] == most_common_bit]
            else:
                copy = copy[copy[:,i] != most_common_bit]

            i += 1

        return bitarr_to_int(copy[0])


    return calc(data, True) * calc(data, False)

def bitarr_to_int(bit_arr: np.array) -> int:
    return bit_arr.dot(2**np.arange(bit_arr.size)[::-1])


data = init()
print(f"1.) {task1(data)}\t2.) {task2(data)}")