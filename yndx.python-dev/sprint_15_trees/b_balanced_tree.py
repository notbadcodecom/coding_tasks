# Гоше очень понравилось слушать рассказ Тимофея про деревья. Особенно часть
# про сбалансированные деревья. Он решил написать функцию, которая определяет,
# сбалансировано ли дерево. Дерево считается сбалансированным, если левое и
# правое поддеревья каждого узла отличаются по высоте не больше, чем на один.
#
# Формат ввода
# На вход функции подается корень бинарного дерева.
# Python:
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left
# Ваша функция должна иметь сигнатуру solution(Node root) -> bool.
# Формат вывода
# Функция должна вернуть True, если дерево сбалансировано в соответствии
# с критерием из условия, иначе - False.

def get_depth(node, depth=0):
    if node is not None:
        depth = max(get_depth(node.left), get_depth(node.right)) + 1
    return depth

def solution(node) -> bool:
    if node is None:
        return True
    right_depths = (-1, 0, 1)
    depth = get_depth(node.left) - get_depth(node.right)
    if depth in right_depths and solution(node.left) and solution(node.right):
        return True
    return False
