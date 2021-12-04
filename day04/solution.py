#!/usr/bin/env python3
import os, sys
import numpy as np

def init() -> tuple[np.array, np.array]:
    # change working dir
    os.chdir(os.path.dirname(sys.argv[0]))

    # load data
    with open("input", "r") as f:
        raw = f.readlines()

        # extract first row as float32-np.array
        draws = np.fromiter([s for s in raw.pop(0).split(",")], dtype=np.float32)

        # convert bingo boards into np.array of dim (#boards, 5, 5)
        boards = np.zeros((len(raw) // 6,5,5))

        for i,s in enumerate(raw):
            if i % 6 != 0: # == 0 is an empty row
                # add row as float32-row to board in boards-array
                boards[i // 6, (i % 6) - 1] = s.strip().split()

    return (draws, boards)

def task1(draws: np.array, boards: np.array) -> int:
    for draw in draws:
        # set all elements that are equal to draw to inf
        boards[boards==draw] = np.inf
        bingo = check_all(boards)

        if bingo >= 0: # not negative implies a bingo
            return int(score(boards[bingo], draw))

    return 0 # no winner

def task2(draws: np.array, boards: np.array) -> int:
    # np.array to keep track which boards one first, second, etc.
    # and with which score
    scores = np.zeros((boards.shape[0],2))

    for j,board in enumerate(boards):
        for i,draw in enumerate(draws):
            # set all elements that are equal to draw to inf
            board[board==draw] = np.inf

            if check_single(board): # implies a bingo
                scores[j,] = [i, score(board, draw)]
                break # stop inner for loop, move to next board

    return scores[np.argmax(scores[:,0])][1] # equal to 0 if no winner

def check_all(boards: np.array) -> int:
    # create inf-vector [inf, inf, inf, inf, inf]
    checkmask = np.empty((5,))
    checkmask[:] = np.inf

    for j,board in enumerate(boards):
        for i in range(0, 5):
            # check for vertical and horizontal inf-vector
            if np.all(board[i] == checkmask) or np.all(board[:,i] == checkmask):
                return j # board index
    
    return -1

def check_single(board: np.array) -> bool:
    # create inf-vector [inf, inf, inf, inf, inf]
    checkmask = np.empty((5,))
    checkmask[:] = np.inf

    for i in range(0, 5):
        # check for vertical and horizontal inf-vector
        if np.all(board[i] == checkmask) or np.all(board[:,i] == checkmask):
            return True

    return False

def score(board: np.array, draw: int) -> int:
    # sum up elements that aren't inf, multiply by draw
    return np.sum(board[board != np.inf]) * draw


(draws, boards) = init()
print(f"1.) {task1(draws, boards)}\t2.) {task2(draws, boards)}")