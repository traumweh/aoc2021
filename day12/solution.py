#!/usr/bin/env python3

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            lines = f.readlines()

        self.data = dict()

        for line in lines:
            edge = line.strip().split("-")

            if edge[1] != "start": # ignore edges to the start
                if edge[0] in self.data: self.data[edge[0]].append(edge[1])
                else: self.data[edge[0]] = [edge[1]]
            if edge[0] != "start": # ignore edges to the start
                if edge[1] in self.data: self.data[edge[1]].append(edge[0])
                else: self.data[edge[1]] = [edge[0]]

        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        self.task1 = 0
        tmp_paths = [["start"]]

        while len(tmp_paths) > 0:
            new_paths = []

            for path in tmp_paths:
                for node in self.data[path[-1]]:
                    if node == "end": self.task1 += 1
                    elif len(path) == 1 or not node.islower() \
                            or node.islower() and not node in path:
                        new_paths.append(path + [node])

            tmp_paths = new_paths

    def __task2(self) -> int:
        self.task2 = 0
        tmp_paths = [(False, ["start"])]

        while len(tmp_paths) > 0:
            new_paths = []

            for path in tmp_paths:
                for node in self.data[path[1][-1]]:
                    if node == "end": self.task2 += 1
                    elif len(path) == 1 or not node.islower() \
                            or (node.islower() and not node in path[1]):
                        new_paths.append((path[0], path[1] + [node]))
                    elif node.islower() and node in path[1] and not path[0]:
                        new_paths.append((True, path[1] + [node]))

            tmp_paths = new_paths

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))