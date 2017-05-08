"""
Высота дерева

Вычислить высоту данного дерева.
Вход.
Корневое дерево с вершинами {0,.., n-1}, заданное как последовательность
parent 0, .., parent n-1, где parent i — родитель i-й вершины.
Выход.
Высота дерева

Две версии:
search_recursion - поиск с помощью рекурсии, при этом
увеличен рекурсивный стек
search_que - итеративный поиск с помощью очереди

"""

from collections import defaultdict
import sys
sys.setrecursionlimit(50000)

def search_height(c, tree):
    height = 1
    if c not in tree:
        return height
    else:
        for val in tree[c]:
            height = max(height, 1 + search_height(val, tree))
    return height 

def search_recursion ():
    tree = defaultdict(list)
    n = int(input())
    nodes = [int(i) for i in input().split()]
    for i, node in enumerate(nodes):
        tree[node].append(i)

    h = search_height(tree[-1][0], tree)

    print(h)

def search_que():
    tree = defaultdict(list)
    result = {}
    n = int(input())
    nodes = [int(i) for i in input().split()]
    for i, node in enumerate(nodes):
        tree[node].append(i)
        if node == -1:
            root = i
    que = [root]
    result[root] = 1
    while que:
        elem = que.pop(0)
        if elem in tree:
            for node in tree[elem]:
                result[node] = result[elem] + 1
                que.append(node)
    print (max(result.values()))

if __name__ == "__main__":
    search_recursion()
    search_que()


