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
    global clock
    visited = [False] * (2 * n + 1)
    post = [0] * (2 * n + 1)
    for v in range(1, 2 * n + 1):
        if not visited[v]:
            post_order(v, graph, visited, post)
    post = list(enumerate(post[1:], start=1))
    post.sort(key=lambda x:x[1], reverse=True)
    post_vertex = []
    for v, order in post:
        post_vertex.append(v)
    return post_vertex


def explore(i, graph, visited, SCC, SCC_number, u):
    visited[i] = True
    SCC.append(i)
    SCC_number[i] = u
    for v in graph[i]:
        if not visited[v]:
            explore(v, graph, visited, SCC, SCC_number, u)


def find_SCCs(n, rev_graph, graph):
    global clock
    post_vertex = DFS(n, rev_graph)
    visited = [False] * (2 * n + 1)
    SCCs = []
    SCC_number = [0] * (2 * n + 1)
    u = 1
    for i in post_vertex:
        if not visited[i]:
            SCC = []
            explore(i, graph, visited, SCC, SCC_number, u)
            SCCs.append(SCC)
            u += 1
    return SCCs, SCC_number


def two_SAT(n, rev_graph, graph):
    pass


clock = 1
def main():
    pass

# This is to avoid stack overflow issues
threading.Thread(target=main).start()
