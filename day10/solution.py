#!/usr/bin/env python3

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = f.readlines()

        self.__tasks()

    def __tasks(self) -> tuple:
        closing = {"(": ")","[": "]","{": "}","<": ">"}
        illegal_points = {")": 3,"]": 57,"}": 1197,">": 25137}
        incomplete_points = {"(": 1,"[": 2,"{": 3,"<": 4}
        self.task1 = 0
        scores = list()

        for line in self.data:
            stack = list()

            for c in line.strip():
                if c in ["(","[","{","<"]:
                    stack.append(c)
                elif closing[stack[-1]] == c:
                    stack.pop(-1)
                else:
                    self.task1 += illegal_points[c]
                    stack = list()
                    break

            if len(stack) > 0:
                score = 0

                for c in reversed(stack):
                    score = score * 5 + incomplete_points[c]
            
                scores.append(score)

        self.task2 = sorted(scores)[(len(scores))//2]

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))