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

    def __add__(self, other):
        matrix_add = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix[0])):
                line.append(self.matrix[i][j] + other.matrix[i][j])
            matrix_add.append(line)
        return Matrix(matrix_add)

    def __mul__(self, other):
        matrix_mul = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix[0])):
                line.append(self.matrix[i][j] * other)
            matrix_mul.append(line)
        return Matrix(matrix_mul)

    __rmul__ = __mul__


exec(stdin.read())
