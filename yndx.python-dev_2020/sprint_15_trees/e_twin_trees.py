# Евлампии на день рождения подарили два дерева. Кондратий сказал, что они
# совершенно одинаковые. Но, по мнению Евлампии, они отличаются.
# Помогите разрешить семейный спор!
#
# Формат ввода
# На вход подаются корни двух деревьев.
# Класс, представляющий узел дерева.
# Python:
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left
# Ваша функция должна иметь сигнатуру solution(root1: Node, root2: Node) -> bool.
#
# Формат вывода
# Функция должна вернуть True если деревья являются близнецами. Иначе - False.


def solution(root_one, root_two) -> bool:
    if root_one is None and root_two is None:
        return True
    elif root_one and root_two:
        checking_value = root_one.value == root_two.value
        checking_left = solution(root_one.left, root_two.left)
        checking_right = solution(root_one.right, root_two.right)
        return checking_value and checking_left and checking_right
    return False
