#!/usr/bin/env python3
import json

class Snailfish_Number:
    def __init__(self, element=None, parent: "Snailfish_Number"=None, 
                left: "Snailfish_Number"=None, right: "Snailfish_Number"=None,
                value: int=0):

        if element is not None:
            self.parent = parent

            if type(element) == int:
                self.left = None
                self.right = None
                self.value = element
            else:
                (left, right) = element
                self.left = Snailfish_Number(element=left, parent=self)
                self.right = Snailfish_Number(element=right, parent=self)
                self.value = 0
        else:
            self.parent = parent
            self.left = left
            self.right = right
            self.value = value

    def __add__(self, other: "Snailfish_Number") -> "Snailfish_Number":
        snfn = Snailfish_Number(left=self, right=other)
        snfn.left.parent = snfn
        snfn.right.parent = snfn

        snfn.explode()
        while snfn.split():
            snfn.explode()
        
        return snfn

    def explode(self, depth: int=0):
        if self.left is None and self.right is None:
            return

        if depth >= 4:
            self.parent.addl(self.left.value, self, True)
            self.parent.addr(self.right.value, self, True)
            self.value = 0
            self.left = None
            self.right = None
        else:
            self.left.explode(depth + 1)
            self.right.explode(depth + 1)

    def split(self) -> bool:
        if self.value >= 10:
            left_value = self.value // 2
            right_value = self.value - left_value
            self.left = Snailfish_Number(parent=self, value=left_value)
            self.right = Snailfish_Number(parent=self, value=right_value)
            self.value = 0
            return True
        if self.left is not None:
            if self.left.split():
                return True
        if self.right is not None:
            if self.right.split():
                return True

        return False

    def addl(self, value: int, snfn: "Snailfish_Number", 
                add_to_left_child: bool):
        if add_to_left_child:
            if self.left is not None and self.left is not snfn:
                self.left.addl(value, self, False)
            elif self.parent is not None:
                self.parent.addl(value, self, True)
            else: # no left value
                return
        elif self.right is None:
            self.value += value
        else:
            self.right.addl(value, self, False)

    def addr(self, value: int, snfn: "Snailfish_Number", 
                add_to_right_child: bool):
        if add_to_right_child:
            if self.right is not None and self.right is not snfn:
                self.right.addr(value, self, False)
            elif self.parent is not None:
                self.parent.addr(value, self, True)
            else: # no right value
                return
        elif self.left is None:
            self.value += value
        else:
            self.left.addr(value, self, False)

    def magnitude(self) -> int:
        if self.left is not None and self.right is not None:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()
        else:
            return self.value

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            lines = f.readlines()

        result = list()

        for line in lines:
            line = json.loads(line.strip())
            result.append(line)

        self.data = result
        self.__task1()
        self.__task2()

    def __task1(self) -> int:
        snailfish_sum = Snailfish_Number(element=self.data[0])

        for i in range(1, len(self.data)):
            snailfish_sum += Snailfish_Number(element=self.data[i])

        self.task1 = snailfish_sum.magnitude()

    def __task2(self) -> int:
        self.task2 = 0

        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if i != j:
                    sumij = Snailfish_Number(self.data[i]) \
                            + Snailfish_Number(self.data[j])
                    self.task2 = max(self.task2, sumij.magnitude())

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))