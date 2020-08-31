# Гуляя по вилле Кондратия, ребята нашли генеалогическое древо его семьи.
# Им стало интересно, сколько лет прожили члены семьи разных поколений.
# Помогите ребятам это выяснить.
#
# Формат ввода
# В этом задании нужно реализовать функцию. На вход она принимает голову дерева.

# Python:
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left
# Ваша функция должна иметь сигнатуру solution(root: Node) -> int[][]
# from collections import deque

def solution(root):
    path = []
    queue = [root]
    while queue != []:
        childrens = []
        generation = []
        for elem in queue:
            generation.append(elem.value)
            if elem.left:
                childrens.append(elem.left)
            if elem.right:
                childrens.append(elem.right)
        queue = childrens
        path.append(generation)
    return path
