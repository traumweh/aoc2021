#!/usr/bin/env python3

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = f.readlines()

        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        self.task1 = 0

    def __task2(self) -> int:
        self.task2 = 0

    def __repr__(self) -> str:
        return f"1.) {self.task1}\t2.) {self.task2}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))