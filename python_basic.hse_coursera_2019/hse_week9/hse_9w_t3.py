from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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
        if len(self.matrix) == len(other.matrix):
            for row in self.matrix:
                if len(row) != len(self.matrix[0]):
                    raise MatrixError(self, other)
            for row2 in other.lists:
                if len(row2) != len(self.matrix[0]):
                    raise MatrixError(self, other)
        matrix_add = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix[0])):
                line.append(self.matrix[i][j] + other.matrix[i][j])
            matrix_add.append(line)
        return Matrix(matrix_add)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        matrix_mul = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix[0])):
                line.append(self.matrix[i][j] * other)
            matrix_mul.append(line)
        return Matrix(matrix_mul)

    __rmul__ = __mul__

    @staticmethod
    def transposed(m):
        return Matrix(list(map(list, zip(*m.list))))

    def transpose(self):
        newList = list(map(list, zip(*self.list)))
        self.list = newList
        return self


exec(stdin.read())
