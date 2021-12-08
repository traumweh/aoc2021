#!/usr/bin/env python3
import os, sys

def init() -> list:
    # change working dir
    os.chdir(os.path.dirname(sys.argv[0]))

    # load data
    with open("input", "r") as f:
        data = [[a.split(), b.split()] for a,b in [line.split(" | ") for line in f.readlines()]]

    return data

def task1(data: list) -> int:
    return sum([1 for line in data for b in line[1] if len(b) in [2,3,4,7]])

def task2(data: list) -> int:
    c = 0

    for line in data:
        segments = [None]*10
        unsure = []

        for a in line[0]:
            la = sorted(list(a))

            if len(a) == 2: # obviously 1
                segments[1] = la
            elif len(a) == 3: # obviously 7
                segments[7] = la
            elif len(a) == 4: # obviously 4
                segments[4] = la
            elif len(a) == 7: # obviously 8
                segments[8] = la
            elif la not in unsure: # put aside for now
                unsure.append(la)

        for s in unsure:
            if len(s) == 6: # => 0, 6 or 9
                # are the right vertical segments on => 0 or 9
                if len(set(segments[1] + s)) == 6:
                    # if len unchanged the middle segment must be on => 9
                    if len(set(segments[4] + s)) == 6:
                        segments[9] = s
                    else: # => 0
                        segments[0] = s
                else: # => 6
                    segments[6] = s
            elif len(s) == 5: # => 2, 3 or 5
                # are the right vertical segments on => 3
                if len(set(segments[1] + s)) == 5:
                    segments[3] = s
                # 2 and 4 share two segments => len(segments[2]) + 2
                elif len(set(segments[4] + s)) == 7:
                    segments[2] = s
                # 4 and 5 share three segments => len(segments[2]) + 1
                else:
                    segments[5] = s

        for i,a in enumerate(reversed(line[1])):
            c += 10**i * segments.index(sorted(a))

    return c

data = init()
print(f"1.) {task1(data)}\t2.) {task2(data)}")