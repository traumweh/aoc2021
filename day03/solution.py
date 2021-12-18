#!/usr/bin/env python3
import numpy as np

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = np.array([np.array(l).astype(np.int32) for l in
                    [list(line.strip()) for line in f.readlines()]])

        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        gamma_bits = np.round(np.mean(self.data, axis=0)).astype(np.int32)
        gamma = self.__bitarr_to_int(gamma_bits)
        epsilon = self.__bitarr_to_int(1 - gamma_bits)

        # return power consumption
        self.task1 = gamma * epsilon

    def __task2(self) -> int:
        self.task2 = self.__task2_calc(True) * self.__task2_calc(False)

    def __task2_calc(self, oxygen: bool) -> int:
        copy = self.data.copy()
        i = 0

        while len(copy) > 1:
            zeros = np.sum(1 - copy[:,i], axis=0)
            ones = np.sum(copy[:,i], axis=0)
            most_common_bit = 1 if ones >= zeros else 0

            if oxygen: copy = copy[copy[:,i] == most_common_bit]
            else: copy = copy[copy[:,i] != most_common_bit]

            i += 1

        return self.__bitarr_to_int(copy[0])

    def __bitarr_to_int(self, bit_arr: np.array) -> int:
        return bit_arr.dot(2**np.arange(bit_arr.size)[::-1])

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))