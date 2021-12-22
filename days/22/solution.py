#!/usr/bin/env python3
import re

class Tasks:
    def __init__(self, filepath):
        self.data = list()

        with open(filepath, "r") as f:
            for line in f.readlines():
                r = re.findall(r"(-?\d+)", line)
                self.data.append((line.startswith("on"), (int(r[0]), int(r[1])),
                        (int(r[2]), int(r[3])), (int(r[4]), int(r[5]))))

        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        ranges = list()

        # filter data to interval [-50;50]
        for d in self.data:
            if all(abs(x) < 50 for x in (*d[1], *d[2], *d[3])):
                ranges.append(d)

        self.task1 = self.__count_on(ranges)

    def __task2(self) -> int:
        self.task2 = self.__count_on(self.data)

    def __count_on(self, ranges: list) -> int:
        on = dict()

        for s,xr,yr,zr in ranges:
            tmp = on.copy()
            if s: tmp[(xr,yr,zr)] = s
            
            for (oxr,oyr,ozr),os in on.items(): # o = other
                # i = intersection
                ixr = (max(xr[0],oxr[0]), min(xr[1],oxr[1]))
                iyr = (max(yr[0],oyr[0]), min(yr[1],oyr[1]))
                izr = (max(zr[0],ozr[0]), min(zr[1],ozr[1]))

                if ixr[0] <= ixr[1] and iyr[0] <= iyr[1] and izr[0] <= izr[1]:
                    if (ixr,iyr,izr) in tmp: tmp[(ixr,iyr,izr)] -= os
                    else: tmp[(ixr,iyr,izr)] = -os

            on = tmp

        return sum(self.__count(item) for item in on.items())

    def __count(self, item) -> int:
        (xr, yr, zr), s = item
        return (xr[1]+1 - xr[0]) * (yr[1]+1 - yr[0]) * (zr[1]+1 - zr[0]) * s

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))