#!/usr/bin/env python3
import os, sys
from types import LambdaType
import numpy as np
from scipy.ndimage import minimum_filter

def init() -> np.array:
    # change working dir
    os.chdir(os.path.dirname(sys.argv[0]))

    # load data
    with open("input", "r") as f:
        data = np.array([list(line.strip()) for line in f.readlines()], dtype=np.float32)

    return data

def task1(data: np.array) -> int:
    # get indices of lowpoints and transpose to use as indices for data
    lowpoints = data[tuple(indices_lowpoints(data).T)]
    # sum up the lowpoint-heights and add the number of lowpoints
    return int(sum(lowpoints, len(lowpoints)))

def task2(data: np.array) -> int:
    # create inf-padded (bordered) copy of data to prevent index out of bounds
    padded = np.pad(data, pad_width=1, mode="constant", constant_values=np.inf)
    # get array with sizes of all basins
    basin_sizes = np.fromiter(
        map(
            lambda pos: len(basin(padded, *pos)), # calculate basin size
            indices_lowpoints(data) + 1 # +1 to adjust for padding
        ),
        dtype=np.uint64
    )

    # calculate product of three largest basin sizes
    # using partition is faster than actual sorting (worst-case O(n))
    # because it doesn't actually sort but only makes sure that the
    # first k elements are the k smallest elements and that the 
    # k-th element is the actual k smallest element
    return np.prod(np.partition(basin_sizes, -3)[-3:])

def indices_lowpoints(data: np.array) -> np.array:
    # a bit faster than using nested python-forloops
    # the np.asarray line is a cross-filtermask to check if the masked center is
    # smaller than the rest of the masked elements.
    return np.argwhere(data < minimum_filter(
        data, footprint=np.asarray([[0,1,0],[1,0,1],[0,1,0]]),
        mode="constant", cval=np.inf
    ))

def basin(data: np.array, x: int, y: int) -> set[tuple]:
    c = {(x,y)} # initial set

    # do for above, left, right and below value
    for a,b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        if 9 > data[a,b] > data[x,y]:
            # add to set (thereby ignores duplicates)
            c = c.union(basin(data, a, b))

    return c

data = init()
print(f"1.) {task1(data)}\t2.) {task2(data)}")