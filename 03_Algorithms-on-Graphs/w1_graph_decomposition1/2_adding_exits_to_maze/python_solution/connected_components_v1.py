#Uses python3

import sys

def explore(adj, visited, x):
    visited[x] = True
    for vertex in adj[x]:
        if not visited[vertex]:
            explore(adj, visited, vertex)       # recursive call

def number_of_components(n_vertices, adj, visited):
    result = 0
    for i in range(1, n_vertices + 1):
        if not visited[i]:
            explore(adj, visited, i)
            result += 1
            # print('vertex: ', i, result)
    return result

if __name__ == '__main__':
    # TEST 2
    n_vertices, n_edges = map(int, input().split())
    edges = []
    adj_list = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        edges.append(tuple(map(int, input().split())))
    for (a, b) in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    visited = [False] * (n_vertices + 1)
    n_components = number_of_components(n_vertices, adj_list, visited)
    print(n_components)

    # TEST 1
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    #     adj[b - 1].append(a - 1)
    # print(number_of_components(adj))
