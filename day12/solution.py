#!/usr/bin/env python3
import os, sys

def init() -> list:
    os.chdir(os.path.dirname(sys.argv[0])) # change working dir

    with open("input", "r") as f:
        data = dict()

        for line in f.readlines():
            edge = line.strip().split("-")

            if edge[1] != "start": # ignore edges to the start
                if edge[0] in data: data[edge[0]].append(edge[1])
                else: data[edge[0]] = [edge[1]]
            if edge[0] != "start": # ignore edges to the start
                if edge[1] in data: data[edge[1]].append(edge[0])
                else: data[edge[1]] = [edge[0]]

        return data

def task1(data: list) -> int:
    task1 = 0
    tmp_paths = [["start"]]

    while len(tmp_paths) > 0:
        new_paths = []

        for path in tmp_paths:
            for node in data[path[-1]]:
                if node == "end": task1 += 1
                elif len(path) == 1 or not node.islower() \
                        or node.islower() and not node in path:
                    new_paths.append(path + [node])

        tmp_paths = new_paths

    return task1

def task2(data: list) -> int:
    task2 = 0
    tmp_paths = [(False, ["start"])]

    while len(tmp_paths) > 0:
        new_paths = []

        for path in tmp_paths:
            for node in data[path[1][-1]]:
                if node == "end": task2 += 1
                elif len(path) == 1 or not node.islower() \
                        or (node.islower() and not node in path[1]):
                    new_paths.append((path[0], path[1] + [node]))
                elif node.islower() and node in path[1] and not path[0]:
                    new_paths.append((True, path[1] + [node]))

        tmp_paths = new_paths

    return task2

data = init()
print(f"1.) {task1(data)}\t2.) {task2(data)}")