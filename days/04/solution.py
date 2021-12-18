#!/usr/bin/env python3
import numpy as np

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            raw = f.readlines()

        # extract first row as float32-np.array
        self.draws = np.fromiter([s for s in raw.pop(0).split(",")], 
                    dtype=np.float32)

        # convert bingo boards into np.array of dim (#boards, 5, 5)
        self.boards = np.zeros((len(raw) // 6,5,5))

        for i,s in enumerate(raw):
            if i % 6 != 0: # == 0 is an empty row
                # add row as float32-row to board in boards-array
                self.boards[i // 6, (i % 6) - 1] = s.strip().split()

        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        self.task1 = 0 # no winner

        for draw in self.draws:
            # set all elements that are equal to draw to inf
            self.boards[self.boards == draw] = np.inf
            bingo = self.__check_all()

            if bingo >= 0: # not negative implies a bingo
                self.task1 = int(self.__score(self.boards[bingo], draw))
                break

    def __task2(self) -> int:
        # np.array to keep track which boards one first, second, etc.
        # and with which score
        scores = np.zeros((self.boards.shape[0],2))

        for j,board in enumerate(self.boards):
            for i,draw in enumerate(self.draws):
                # set all elements that are equal to draw to inf
                board[board == draw] = np.inf

                if self.__check_single(board): # implies a bingo
                    scores[j,] = [i, self.__score(board, draw)]
                    break # stop inner for loop, move to next board

        # equal to 0 if no winner
        self.task2 = int(scores[np.argmax(scores[:,0])][1])

    def __check_all(self) -> int:
        # create inf-vector [inf, inf, inf, inf, inf]
        checkmask = np.empty((5,))
        checkmask[:] = np.inf

        for j,board in enumerate(self.boards):
            for i in range(0, 5):
                # check for vertical and horizontal inf-vector
                if np.all(board[i] == checkmask) or \
                            np.all(board[:,i] == checkmask):
                    return j # board index
        
        return -1

    def __check_single(self, board: np.array) -> bool:
        # create inf-vector [inf, inf, inf, inf, inf]
        checkmask = np.empty((5,))
        checkmask[:] = np.inf

        for i in range(0, 5):
            # check for vertical and horizontal inf-vector
            if np.all(board[i] == checkmask) or \
                        np.all(board[:,i] == checkmask):
                return True

        return False

    def __score(self, board: np.array, draw: int) -> int:
        # sum up elements that aren't inf, multiply by draw
        return np.sum(board[board != np.inf]) * draw

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))