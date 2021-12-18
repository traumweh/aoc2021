#!/usr/bin/env python3
import numpy as np
from scipy.ndimage import minimum_filter

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = np.array([list(line.strip()) for line in f.readlines()],
                    dtype=np.float32)

        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        # get indices of lowpoints and transpose to use as indices for data
        lowpoints = self.data[tuple(self.__indices_lowpoints().T)]
        # sum up the lowpoint-heights and add the number of lowpoints
        self.task1 = int(sum(lowpoints, len(lowpoints)))

    def __task2(self) -> int:
        # create inf-padded copy of data to prevent index out of bounds
        padded = np.pad(self.data, pad_width=1, mode="constant", 
                constant_values=np.inf)
        # get array with sizes of all basins
        basin_sizes = np.fromiter(
            map(
                lambda pos: len(self.__basin(padded, *pos)), # basin size
                self.__indices_lowpoints() + 1 # +1 to adjust for padding
            ),
            dtype=np.uint64
        )

        # calculate product of three largest basin sizes
        # using partition is faster than actual sorting (worst-case O(n))
        # because it doesn't actually sort but only makes sure that the
        # first k elements are the k smallest elements and that the 
        # k-th element is the actual k smallest element
        self.task2 = np.prod(np.partition(basin_sizes, -3)[-3:])

    def __indices_lowpoints(self) -> np.array:
        # a bit faster than using nested python-forloops
        # the np.asarray line is a cross-filtermask to check if the masked 
        # center is smaller than the rest of the masked elements.
        return np.argwhere(self.data < minimum_filter(
            self.data, footprint=np.asarray([[0,1,0],[1,0,1],[0,1,0]]),
            mode="constant", cval=np.inf
        ))

    def __basin(self, padded: np.array, x: int, y: int) -> set[tuple]:
        result = {(x,y)} # initial set

        # do for above, left, right and below value
        for a,b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 9 > padded[a,b] > padded[x,y]:
                # add to set (thereby ignores duplicates)
                result = result.union(self.__basin(padded, a, b))

        return result

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))