#!/usr/bin/env python3
import os, sys

closing = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

illegal_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

incomplete_points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

def init() -> list:
    # change working dir
    os.chdir(os.path.dirname(sys.argv[0]))

    # load and int-cast data
    with open("input", "r") as f:
        data = f.readlines()

    return data

def task1(data: list) -> int:
    score = 0

    for line in data:
        score += illegal(line.strip(), [])

    return score

def task2(data: list) -> int:
    data = data.copy()
    scores = []

    for i,line in enumerate(data):
        if illegal(line.strip(), []) > 0:
            data.pop(i)

    for line in data:
        c = incomplete(line.strip(), [])
        if c > 0:
            scores.append(c)

    return sorted(scores)[(len(scores))//2]

def illegal(line: str, stack: list) -> int:
    if len(line) > 0:
        first = line[0]

        if first in ["(","[","{","<"]:
            stack.append(first)
            return illegal(line[1:], stack)
        elif closing[stack[-1]] == first:
            return illegal(line[1:], stack[:-1])
        else:
            return illegal_points[first]

    return 0

def incomplete(line: str, stack: list) -> int:
    if len(line) > 0:
        first = line[0]

        if first in ["(","[","{","<"]:
            stack.append(first)
            return incomplete(line[1:], stack)
        elif closing[stack[-1]] == first:
            stack.pop(-1)
            return incomplete(line[1:], stack)

        return 0

    score = 0

    for c in reversed(stack):
        score = score * 5 + incomplete_points[c]
    
    return score


data = init()
print(f"1.) {task1(data)}\t2.) {task2(data)}")