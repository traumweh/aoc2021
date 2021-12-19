#!/usr/bin/env python3
from itertools import starmap

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            lines = f.readlines()
        
        self.data = list()

        for line in lines:
            if "---" in line:
                self.data.append(list())
            elif line.strip():
                row = tuple(map(int, line.split(",")))
                self.data[-1].append(row)

        self.__orientations = [lambda x,y,z: (x,y,z),
                             lambda x,y,z: (-x,y,z),
                             lambda x,y,z: (-x,-y,z),
                             lambda x,y,z: (-x,y,-z),
                             lambda x,y,z: (-x,-y,-z),
                             lambda x,y,z: (x,-y,z),
                             lambda x,y,z: (x,-y,-z),
                             lambda x,y,z: (x,y,-z)]
        self.__facings = [lambda x,y,z: (x,y,z),
                        lambda x,y,z: (y,x,z),
                        lambda x,y,z: (z,y,x),
                        lambda x,y,z: (x,z,y),
                        lambda x,y,z: (y,z,x),
                        lambda x,y,z: (z,x,y)]
        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        self.__done_scanners = [(0,0,0)]
        self.__done_beacons = set(self.data[0])
        self.__not_done = self.data[1:]

        self.__fix_multiple()
        self.task1 = len(self.__done_beacons)

    def __task2(self) -> int:
        distance = 0

        for xi, yi, zi in self.__done_scanners:
            for xj, yj, zj in self.__done_scanners:
                new_distance = abs(xj - xi) + abs(yj - yi) + abs(zj - zi)
                distance = max(distance, new_distance)

        self.task2 = distance

    def __fix_multiple(self):
        while self.__not_done:
            for scanner in self.__not_done:
                beacons, location = self.__fix_single(scanner)

                if beacons:
                    self.__not_done.remove(scanner)
                    self.__done_scanners.append(location)
                    self.__done_beacons = self.__done_beacons.union(beacons)

    def __fix_single(self, scanner: list) -> tuple:
        for orientation in self.__orientations:
            for facing in self.__facings:
                beacons = set(starmap(facing, starmap(orientation, scanner)))
                beacons, location = self.__align(beacons)

                if beacons: return beacons, location
        
        return None, None

    def __align(self, beacons: set) -> tuple:
        for i in range(3):
            dbs = sorted(self.__done_beacons, key=lambda x: x[i])
            bcs = sorted(beacons, key=lambda x: x[i])
            delta_dbs = list()
            delta_beacons = list()

            for j in range(1,len(dbs)):
                delta_dbs.append(self.__delta(dbs[j], dbs[j-1]))

            for j in range(1,len(bcs)):
                delta_beacons.append(self.__delta(bcs[j], bcs[j-1]))

            intersection = set(delta_dbs).intersection(set(delta_beacons))

            if intersection:
                difference = intersection.pop()
                sc_loc = dbs[delta_dbs.index(difference)]
                be_loc = bcs[delta_beacons.index(difference)]
                orig = self.__delta(sc_loc,be_loc)
                aligned = {self.__delta(orig,b) for b in bcs}
                intersection = self.__done_beacons.intersection(aligned)

                if len(intersection) >= 12:
                    return aligned, orig
        
        return None, None

    def __delta(self, a, b):
        return b[0]-a[0],b[1]-a[1],b[2]-a[2]

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))