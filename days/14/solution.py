#!/usr/bin/env python3

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            lines = f.readlines()

        template = lines[0].strip()
        self.elements = dict()
        self.rules = dict()

        for line in lines[2:]:
            line = line.strip().split(" -> ")
            self.elements[line[1]] = 0
            self.rules[line[0]] = line[1]

        self.pairs = {rule:0 for rule in self.rules.keys()}

        for i in range(len(template) - 1):
            self.pairs[template[i:i+2]] += 1
            self.elements[template[i]] += 1

        self.elements[template[-1]] += 1
        self.__tasks()

    def __tasks(self) -> int:
        self.__calc(10)
        self.task1 = max(self.elements.values()) - min(self.elements.values())

        self.__calc(30)
        self.task2 = max(self.elements.values()) - min(self.elements.values())

    def __calc(self, steps: int,) -> tuple:
        for _ in range(steps):
            for key, val in self.pairs.copy().items():
                new = self.rules[key]

                self.pairs[key] -= val
                self.pairs[key[0] + new] += val
                self.pairs[new + key[1]] += val
                self.elements[new] += val

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))