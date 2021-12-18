#!/usr/bin/env python3
import heapq

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = [list(map(int, line.strip())) for line in f.readlines()]

        self.__tasks()

    def __tasks(self) -> int:
        self.task1 = self.__walk()
        self.task2 = self.__walk(5)

    def __walk(self, actual_size: int=1) -> None:
        xlen = len(self.data)
        ylen = len(self.data[0])
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
                    value = (self.data[x2 % xlen][y2 % ylen] + (x2 // xlen) + \
                        (y2 // ylen) - 1) % 9 + 1
                    # add new position and risk-level to heap queue
                    # heapq sorts by the first element of the tuple (dxy)
                    heapq.heappush(heap, (dxy + value, x2, y2))
                    # and add position to used-nodes set
                    used.add((x2,y2))

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))