#!/usr/bin/env python3
import os, sys

def init() -> list:
    os.chdir(os.path.dirname(sys.argv[0])) # change working dir

    with open("input", "r") as f:
        return f.readlines()

def tasks(data: list) -> tuple:
    return (0,0)

print("1.) {}\t2.) {}".format(*tasks(init())))