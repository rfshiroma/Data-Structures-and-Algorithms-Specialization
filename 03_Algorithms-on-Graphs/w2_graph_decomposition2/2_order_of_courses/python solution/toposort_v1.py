#Uses python3
# Good job! (Max time used: 0.53/10.00, max memory used: 39419904/536870912.)
'''Compute a topological ordering of a given directed acyclic graph (DAG) with n vertices and m edges.'''

import sys

def explore(graph, vertex, visited, post):
    global clock
    visited[vertex] = True
    for v in graph[vertex]:
        if not visited[v]:
            explore(graph, v, visited, post)
    post[vertex] = clock
    clock += 1


def topo_sort(n, graph, visited, post):
    global clock
    for i in range(1, n + 1):
        if not visited[i]:
            explore(graph, i, visited, post)
    post = list(enumerate(post[1:], start=1))
    post.sort(key=lambda x:x[1], reverse=True)          # sort() method change original input sequence (list class)
    return post

if __name__ == '__main__':
    # TEST 2
    n_vertices, n_edges = map(int, input().split())
    edges = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        a, b = map(int, input().split())
        edges[a].append(b)
    visited = [False] * (n_vertices + 1)
    postorder = [0] * (n_vertices + 1)
    clock = 1
    postorder = topo_sort(n_vertices, edges, visited, postorder)
    for v, post in postorder:
        print(v, end=' ')

    # TEST 1
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    # order = toposort(adj)
    # for x in order:
    #     print(x + 1, end=' ')
