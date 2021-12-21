#!/usr/bin/env python3
from importlib import import_module
from time import time

for i in range(1, 22):
    module = import_module(f"days.{i:02}.solution")

    t1 = time()
    solution = module.Tasks(f"days/{i:02}/input")
    dt = time() - t1

    print("Day {:02} (in {:06.03f} s):\t{}".format(i, dt, solution))