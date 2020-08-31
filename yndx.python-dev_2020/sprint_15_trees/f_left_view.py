# # # Прабабке Кондратия уже 182 года. Домна Тарасовна часто любит выходить в сад
# # # погулять. Сегодня, выходя на прогулку, она забыла очки, без которых почти
# # # ничего не видит. Но она может прекрасно ориентироваться при помощи трости.
# # # Ей она и определила, что приближается к дереву. Что бы увидела баба Домна,
# # # если бы не забыла очки?
# #
# # Формат ввода
# # Напишите функцию, которая определяет, что перед бабушкой Кондратия.
# # Python:
# # class Node:
# #     def __init__(self, value, left=None, right=None):
# #         self.value = value
# #         self.right = right
# #         self.left = left
# # Ваша функция должна иметь сигнатуру solution(root: Node) -> int[].
#
# Формат вывода
# Функция должна вернуть список вершин дерева, которые видны, если Домна
# Тарасовна подошла к нему слева.

def solution(root):
    path = []
    queue = [root]
    while queue != []:
        childrens = []
        for elem in queue:
            if elem.left:
                childrens.append(elem.left)
            if elem.right:
                childrens.append(elem.right)
        path.append(queue[0].value)
        queue = childrens
    return path
