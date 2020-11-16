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
    n = len(colors)
    C = []
    for i in range(1, n + 1):
        node = Node(i)
        if colors[i - 1] == 'R':
            # C.append((-node.r))
            C.append((node.g, node.b))
            C.append((-node.g, -node.b))
        elif colors[i - 1] == 'G':
            # C.append((-node.g))
            C.append((node.r, node.b))
            C.append((-node.r, -node.b))
        elif colors[i - 1] == 'B':
            C.append((node.r, node.g))
            C.append((-node.r, -node.g))
    for a, b in edges:
        u, v = Node(a), Node(b)
        C.append((-u.r, -v.r))
        C.append((-u.g, -v.g))
        C.append((-u.b, -v.b))
    return C


def two_SAT_to_graph(n, C):
    graph = [[] for _ in range(2 * n + 1)]
    rev_graph = [[] for _ in range(2 * n + 1)]
    for a, b in C:
        if a > 0 and b > 0:
            graph[a + n].append(b)
            graph[b + n].append(a)
            rev_graph[b].append(a + n)
            rev_graph[a].append(b + n)
        elif a < 0 and b < 0:
            graph[-a].append(-b + n)
            graph[-b].append(-a + n)
            rev_graph[-b + n].append(-a)
            rev_graph[-a + n].append(-b)
        elif a < 0 and b > 0:
            graph[-a].append(b)
            graph[b + n].append(-a + n)
            rev_graph[b].append(-a)
            rev_graph[-a + n].append(b + n)
        elif a > 0 and b < 0:
            graph[a + n].append(-b + n)
            graph[-b].append(a)
            rev_graph[-b + n].append(a + n)
            rev_graph[a].append(-b)
    return graph, rev_graph



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
