#!/usr/bin/env python3
import os, sys

def init() -> list:
    os.chdir(os.path.dirname(sys.argv[0])) # change working dir

    with open("input", "r") as f:
        return f.readlines()

def tasks(data: list) -> tuple:
    closing = {"(": ")","[": "]","{": "}","<": ">"}
    illegal_points = {")": 3,"]": 57,"}": 1197,">": 25137}
    incomplete_points = {"(": 1,"[": 2,"{": 3,"<": 4}
    task1 = 0
    task2 = list()

    for line in data:
        stack = list()

        for c in line.strip():
            if c in ["(","[","{","<"]:
                stack.append(c)
            elif closing[stack[-1]] == c:
                stack.pop(-1)
            else:
                task1 += illegal_points[c]
                stack = list()
                break

        if len(stack) > 0:
            score = 0

            for c in reversed(stack):
                score = score * 5 + incomplete_points[c]
        
            task2.append(score)

    return task1, sorted(task2)[(len(task2))//2]

print("1.) {}\t2.) {}".format(*tasks(init())))