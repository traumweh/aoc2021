#!/usr/bin/env python3
import os, sys

def init() -> tuple:
    os.chdir(os.path.dirname(sys.argv[0])) # change working dir

    with open("input", "r") as f:
        lines = f.readlines()
        template = lines[0].strip()
        rules = dict()
        elements = dict()

        for line in lines[2:]:
            line = line.strip().split(" -> ")
            rules[line[0]] = line[1]
            elements[line[1]] = 0

        pairs = {rule:0 for rule in rules.keys()}

        for i in range(len(template) - 1):
            pairs[template[i:i+2]] += 1
            elements[template[i]] += 1

        elements[template[-1]] += 1
        return pairs, elements, rules

def tasks(pairs: dict, elements: dict, rules: dict) -> tuple:
    pairs, elements = calc(10, pairs, elements, rules)
    task1 = max(elements.values()) - min(elements.values())

    pairs, elements = calc(30, pairs, elements, rules)
    task2 = max(elements.values()) - min(elements.values())

    return (task1,task2)

def calc(steps: int, pairs: dict, elements: dict, rules: dict) -> tuple:
    for _ in range(steps):
        for key, val in pairs.copy().items():
            new = rules[key]

            pairs[key] -= val
            pairs[key[0] + new] += val
            pairs[new + key[1]] += val
            elements[new] += val

    return pairs, elements


print("1.) {}\t2.) {}".format(*tasks(*init())))