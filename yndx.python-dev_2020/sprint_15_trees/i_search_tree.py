# Гоша понял, что такое дерево поиска, и захотел написать функцию, которая
# определяет, является ли заданное дерево деревом поиска. Значения в левом
# поддереве должны быть строго меньше, в правом - строго больше значения в
# узле. Помогите Гоше с реализацией.
#
# Формат ввода
# На вход функции подается корень бинарного дерева.
# Python:
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def solution(root: Node, start=0, end=6000) -> bool:
    if root is None:
        return True
    if root.value < start or root.value > end:
        return False
    left = solution(root.left, start, root.value - 1)
    right = solution(root.right, root.value + 1, end)
    return left and right
