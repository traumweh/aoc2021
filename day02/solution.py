#!/usr/bin/env python3

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = [(s[0], int(s[1])) for s in [line.split(" ") for line
                    in f.readlines()]]

        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        v = h = 0

        for direction, units in self.data:
            if direction == "forward":
                h += units
            elif direction == "up":
                v -= units
            else:
                v += units

        self.task1 = v * h

    def __task2(self) -> int:
        aim = v = h = 0

        for direction, units in self.data:
            if direction == "forward":
                h += units
                v += aim * units
            elif direction == "up":
                aim -= units
            else:
                aim += units

        self.task2 = v*h

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))