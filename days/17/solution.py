#!/usr/bin/env python3
import re

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            r = re.search(r"x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", 
                    f.readline())

        self.xrange = (int(r.group(1)), int(r.group(2)))
        self.yrange = (int(r.group(3)), int(r.group(4)))
        self.__tasks()

    def __tasks(self) -> int:
        self.task1 = 0
        self.task2 = 0

        self.task1 = abs(self.yrange[0]) * abs(self.yrange[0] + 1) // 2
        self.task2 = 0

        for init_x in range(min(0, self.xrange[0]), max(0, self.xrange[1] + 1)):
            for init_y in range(self.yrange[0], abs(self.yrange[0])):
                x = y = 0
                dx = init_x
                dy = init_y

                while y > self.yrange[0]:
                    # add current step
                    x += dx
                    y += dy

                    # adjust for drag and gravity
                    if dx < 0: dx += 1
                    elif dx > 0: dx -= 1
                    dy -= 1

                    # in target area?
                    if self.xrange[0] <= x <= self.xrange[1] and \
                                self.yrange[0] <= y <= self.yrange[1]:
                        self.task2 += 1
                        break # only count unique inital velocities

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))