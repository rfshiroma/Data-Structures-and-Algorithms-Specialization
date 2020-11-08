# python3

import sys
import threading

# Code below is used to avoid stack overflow issues
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def read_tree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)


def DFS(tree, v, parent, D):
    pass


def max_weight_independent_tree_subset(tree):
    pass


def main():
    tree = read_tree()
    weight = max_weight_independent_tree_subset()
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
