#!/usr/bin/env python3
import os, sys, re

def init() -> tuple:
    os.chdir(os.path.dirname(sys.argv[0])) # change working dir

    with open("input", "r") as f:
        r = re.search(r"x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", f.readline())

        if r: return (int(r.group(1)), int(r.group(2))), \
                     (int(r.group(3)), int(r.group(4)))

def tasks(xrange: tuple, yrange: tuple) -> tuple:
    task1 = abs(yrange[0]) * abs(yrange[0] + 1) // 2
    task2 = 0

    for init_x in range(min(0, xrange[0]), max(0, xrange[1] + 1)):
        for init_y in range(yrange[0], abs(yrange[0])):
            x = y = 0
            dx = init_x
            dy = init_y

            while y > yrange[0]:
                # add current step
                x += dx
                y += dy

                # adjust for drag and gravity
                if dx < 0: dx += 1
                elif dx > 0: dx -= 1
                dy -= 1

                # in target area?
                if xrange[0] <= x <= xrange[1] and yrange[0] <= y <= yrange[1]:
                    task2 += 1
                    break # only count unique inital velocities

    return (task1,task2)

print("1.) {}\t2.) {}".format(*tasks(*init())))