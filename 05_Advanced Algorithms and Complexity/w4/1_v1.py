# python3

import sys
import threading

def post_order(i, graph, visited, post):
    global clock
    visited[i] = True
    for v in graph[i]:
        if not visited[v]:
            post_order(v, graph, visited, post)
    post[i] = clock
    clock += 1


def DFS(n, graph):
    pass


def explore(i, graph, visited, SCC, SCC_number, u):
    pass


def find_SCCs(n, rev_graph, graph):
    pass


def two_SAT(n, rev_graph, graph):
    pass


clock = 1
def main():
    pass

# This is to avoid stack overflow issues
threading.Thread(target=main).start()
