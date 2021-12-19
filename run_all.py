#!/usr/bin/env python3
from importlib import import_module

for i in range(1, 20):
    module = import_module(f"days.{i:02}.solution")
    print("Day{:02}:\t{}".format(i, module.Tasks(f"days/{i:02}/input")))