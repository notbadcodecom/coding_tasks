# У Евлампии есть брошь с бриллиантами в виде дерева. В каждом узле дерева
# есть какое-то количество бриллиантов. Помогите выяснить, какое максимальное
# количество бриллиантов есть в одном узле.
# В Трешландии может быть и отрицательное число драгоценных камней в украшении.
#
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left

def solution(Node, max_value=None) -> int:
    if max_value is None:
        max_value = Node.value
    if Node.left:
        max_value = solution(Node.left)
    if Node.right:
        max_value = solution(Node.right)
    return max(max_value, Node.value)
