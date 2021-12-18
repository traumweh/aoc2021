#!/usr/bin/env python3

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = [[a.split(), b.split()] for a,b in [line.split(" | ") 
                    for line in f.readlines()]]

        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        self.task1 = sum([1 for line in self.data for b in line[1] if len(b) in 
                [2,3,4,7]])

    def __task2(self) -> int:
        self.task2 = 0

        for line in self.data:
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
                self.task2 += 10**i * segments.index(sorted(a))

        return self.task2

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))