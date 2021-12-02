#!/usr/bin/env python3
import os, sys

def init() -> list:
    # change working dir
    os.chdir(os.path.dirname(sys.argv[0]))

    # load and int-cast data
    with open("input", "r") as f:
        data = f.readlines()

    return data

def task1(data: list) -> int:
    return 0

def task2(data: list) -> int:
    return 0


data = init()
print(f"1.) {task1(data)}\t2.) {task2(data)}")