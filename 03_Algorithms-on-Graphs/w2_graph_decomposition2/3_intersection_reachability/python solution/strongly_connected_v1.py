#Uses python3
# Good job! (Max time used: 0.02/5.00, max memory used: 9416704/536870912.)

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)   # new thread size which will get stack


def explore(vertex, graph, visited):
    visited[vertex] = True
    for v in graph[vertex]:
        if not visited[v]:
            explore(v, graph, visited)      # recursive call

def explore_clock(vertex, graph, visited, post):
    global clock
    visited[vertex] = True
    clock += 1
    for v in graph[vertex]:
        if not visited[v]:
            explore_clock(v, graph, visited, post)      # recursive call
    post[vertex] = clock
    clock += 1

def DFS(n, graph):
    global clock
    visited = [False] * (n + 1)
    post = [0] * (n + 1)
    for v in range(1, n + 1):
        if not visited[v]:
            explore_clock(v, graph, visited, post)
    post = list(enumerate(post[1:], start=1))
    post.sort(key=lambda x:x[1], reverse=True)
    post_vertex = []
    for v, order in post:
        post_vertex.append(v)
    return post_vertex

def number_of_SCC(n, reverse_graph, graph):
    global clock
    post_vertex = DFS(n, reverse_graph)
    visited = [False] * (n + 1)
    n_SCC = 0
    for i in post_vertex:
        if not visited[i]:
            explore(i, graph, visited)
            n_SCC += 1
    return n_SCC

def main():
    global clock
    n_vertices, n_edges = map(int, input().split())
    edges = [[] for _ in range(n_vertices + 1)]
    reverse_edges = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        a, b = map(int, input().split())
        edges[a].append(b)
        reverse_edges[b].append(a)
    clock = 1
    n_SCC = number_of_SCC(n_vertices, reverse_edges, edges)
    print(n_SCC)


if __name__ == '__main__':
    # TEST 2
    threading.Thread(target=main).start()

    # TEST 1
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    # print(number_of_strongly_connected_components(adj))
