#!/usr/bin/env python3
import os, sys, heapq

def init() -> list:
    os.chdir(os.path.dirname(sys.argv[0])) # change working dir

    with open("input", "r") as f:
        return [list(map(int, line.strip())) for line in f.readlines()]

def tasks(data: list) -> tuple:
    task1 = walk(data, len(data), len(data[0]))
    task2 = walk(data, len(data), len(data[0]), 5)
    return (task1,task2)

def walk(data: list, xlen: int, ylen: int, actual_size: int=1) -> None:
    maxx = xlen * actual_size - 1 # max x index
    maxy = ylen * actual_size - 1 # max y index
    heap = [(0, 0, 0)] # keep track of paths and their risk-levels
    used = {(0,0)} # don't reuse nodes

    while heap: # -> heap not empty
        # retrieve tuple t with smallest t[0] from heap
        dxy, x, y = heapq.heappop(heap) 

        if x == maxx and y == maxy:
            return dxy

        # for all existing nodes around (x,y) that haven't been used yet
        for x2, y2 in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0 <= x2 <= maxx and 0 <= y2 <= maxy and (x2,y2) not in used:
                # get the value via modulo and add remainder to take tile-
                # repititions into account.
                # (d - 1) % 9 + 1 because:
                #     data[x][y] = 9 -> 9 % 9 = 0
                #     but desired result is 9:
                #     (9 - 1) % 9 + 1 = 9
                # Still correct for 0: 0 % 9 = (0 - 1) % 9 + 1
                value = (data[x2 % xlen][y2 % ylen] + (x2 // xlen) + \
                    (y2 // ylen) - 1) % 9 + 1
                # add new position and risk-level to heap queue
                # heapq sorts by the first element of the tuple (dxy)
                heapq.heappush(heap, (dxy + value, x2, y2))
                # and add position to used-nodes set
                used.add((x2,y2))


print("1.) {}\t2.) {}".format(*tasks(init())))