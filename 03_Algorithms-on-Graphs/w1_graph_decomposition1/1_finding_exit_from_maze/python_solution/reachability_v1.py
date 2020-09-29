#Uses python3
# Good job! (Max time used: 0.01/5.00, max memory used: 9633792/536870912.)


import sys

def reach(adj, visited, x, y):
    visited[x] = True
    for vertex in adj[x]:
        if not visited[vertex]:
            reach(adj, visited, vertex, y)          # recursive call

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
    u, v = map(int, input().split())
    visited = [False] * (n_vertices + 1)
    reach(adj_list, visited, u, v)
    if visited[v]:
        print(1)
    else:
        print(0)

    # TEST 1
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # x, y = data[2 * m:]
    # adj = [[] for _ in range(n)]
    # x, y = x - 1, y - 1
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    #     adj[b - 1].append(a - 1)
    # print(reach(adj, x, y))
