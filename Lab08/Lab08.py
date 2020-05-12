import numpy as np


class Node:
    def __init__(self, value):
        self.key = value  # значення ключа
        self.parent = None  # значення батьківського вузла
        self.left = None  # значення лівого потомка
        self.right = None  # значення правого потомка


def in_order_tree_walk(root, inorder):  # функція для обходу дерева приямим шляхом
    if root is None:
        return
    in_order_tree_walk(root.left, inorder)  # обробка лівого піддерева
    inorder.append(root.key)  # копіювання значння кореня
    in_order_tree_walk(root.right, inorder)  # обробка правого піддерева


def BST_from_array(arr, root):  # функція перетворення масиву на дерево пошуку
    if root is None:
        return
    BST_from_array(arr, root.left)  # перетворення лівого піддерева
    root.key = arr[0]  # перевторення значень кореня
    arr.pop(0)  # видалення значень з масиву
    BST_from_array(arr, root.right)  # перетворення правого піддерева


def create_BST(arr):  # функція для перетворення бінарного дерва на бінарне дерево пошуку
    root = tree_help(arr)
    a = []
    in_order_tree_walk(root, a)
    a.sort()  # сортує масив
    BST_from_array(a, root)  # копіювання елементів до бірнарного дерева
    return root


def tree_help(arr):  # допоміжна функція для виводу дерева
    flag = False
    root = arr[0]
    node = Node(root)
    copy = node
    for i in range(1, len(arr)):
        if arr[i] != 0 and not flag:  # робота з лівим піддеревом
            copy.left = Node(arr[i])
            copy.left.parent = copy
            copy = copy.left
        elif arr[i] != 0 and flag:  # робота з правим піддеревом
            copy.right = Node(arr[i])
            copy.right.parent = copy
            copy = copy.right
            flag = False
        elif arr[i] == 0 and not flag:
            flag = True
        else:
            copy = copy.parent  # робота з батьківським вузлом
            try:
                while copy.right is not None:
                    copy = copy.parent
            except AttributeError:
                pass
    return node


def print_in_order(root):  # функція для друку дерева в прямому порядку
    if root is None:
        return
    print_in_order(root.left)  # виклик для лівого піддерева
    print(root.key)
    print_in_order(root.right)  # виклик для правого піддерева


def checkSum(root, s):  # функція дя пошуку заданої суми
    sam = int(0)
    line = str("")
    f = open("output.txt", "a")
    for i in range(len(root)):
        for j in range(i, len(root)):  # прохід по всім значенням масиву
            sam += root[j]  # збільшення значення змінної sum
            line += str(root[j]) + " "
        if sam == s:  # перевірка чи буде наша сума рівною шуканій
            f.write(str(line) + '\n')  # запис до вихідного файлу
            print(temp)
        sam = 0  # очищення змінної суми
        line = ""
    for i in range(len(root) - 1):  # перевірка значень масиву
        if root[i] == s:  # перевірка рівності значень масиву та заданої суми
            print(root[i])
    f.close()


def findSum(x, res, s):  # фунція для знаходження послідовностей в дереві
    global index, temp
    if x < len(arr):
        if temp[x] != 0:
            res.append(temp[x])  # вставка нового значення з поточної вітки
            checkSum(res, s)  # перевірка масиву на нявність в ньому значення шуканої суми
            index += 1
            findSum(index, res, s)  # виклик функція для лівого потомка
            index += 1
            findSum(index, res, s)  # виклик функції для правого потомка
            res.pop()  # видалення поточного значення з дерева


arr = [int(x) for x in (list(open(input('Enter file name: '))))[0].split() if x != ' ']  # зчитування даних з файлу
# print(arr)
temp = np.copy(arr)
tree = create_BST(temp)
print_in_order(tree)
s = 51
index = 0
findSum(0, [], s)
