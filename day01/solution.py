#!/usr/bin/env python3
import os, sys

def init() -> list:
    # change working dir
    os.chdir(os.path.dirname(sys.argv[0]))

    # load and int-cast data
    with open("input", "r") as f:
        data = list(map(lambda x: int(x), f.readlines()))
    return data

def task1(data: list) -> int:
    c = 0

    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            c += 1

    return c

def task2(data: list) -> int:
    prev = sum(data[0:3])
    c = 0

    for i in range(1, len(data) - 2):
        new = sum(data[i:i+3])

        if prev < new:
            c += 1

        prev = new

    return c


data = init()
print(f"1.) {task1(data)}\t2.) {task2(data)}")