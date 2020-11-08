# python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class Node:
    def __init__(self, i):
        self.r = 3 * i - 2
        self.g = 3 * i - 1
        self.b = 3 * i


def reduce_to_two_SAT(color, edges):
    pass


def two_SAT_to_graph(n, C):
    pass


def post_order(i, graph, visited, post):
    pass


def DFS(n, graph):
    pass


def explore(i, graph, visited, SCC, SCC_number, u):
    pass


def find_SCCs(n, rev_graph, graph):
    pass


def solve_two_SAT(n, rev_graph, graph):
    pass

# This is to avoid stack overflow issues
threading.Thread(target=main).start()
