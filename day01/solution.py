#!/usr/bin/env python3

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = list(map(lambda x: int(x), f.readlines()))

        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        self.task1 = 0

        for i in range(1, len(self.data)):
            if self.data[i - 1] < self.data[i]:
                self.task1 += 1

    def __task2(self) -> int:
        prev = sum(self.data[0:3])
        self.task2 = 0

        for i in range(1, len(self.data) - 2):
            new = sum(self.data[i:i+3])

            if prev < new:
                self.task2 += 1

            prev = new

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))