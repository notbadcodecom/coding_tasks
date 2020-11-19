from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        matrix_str = []
        for line in self.matrix:
            matrix_str.append('\t'.join(map(str, line)))
        return '\n'.join(matrix_str)

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))


 exec(stdin.read())
