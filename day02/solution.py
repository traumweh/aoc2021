#!/usr/bin/env python3
import os, sys

def init() -> list:
    # change working dir
    os.chdir(os.path.dirname(sys.argv[0]))

    # load and int-cast data
    with open("input", "r") as f:
        data = [(s[0], int(s[1])) for s in [line.split(" ") for line in f.readlines()]]

    return data

def task1(data: list) -> int:
    v = 0
    h = 0

    for direction, units in data:
        if direction == "forward":
            h += units
        elif direction == "up":
            v -= units
        else:
            v += units

    return v * h

def task2(data: list) -> int:
    aim = 0
    v = 0
    h = 0

    for direction, units in data:
        if direction == "forward":
            h += units
            v += aim * units
        elif direction == "up":
            aim -= units
        else:
            aim += units

    return v*h


data = init()
print(f"1.) {task1(data)}\t2.) {task2(data)}")