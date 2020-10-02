#Uses python3
# Good job! (Max time used: 0.29/10.00, max memory used: 40943616/536870912.)

'''Computing the Minimum Number of Flight Segments'''
# Problem Task: Given an undirected graph with n vertices and m edges and two vertices u and v, compute the length of a shortest path between u and v (taht is, the minimum number of edges in a path from u to v).

import sys
from collections import deque       # Doubly Ended Queue


def BFS(n, adj, start, end):
    dist = [float('inf')] * (n + 1)
    queue = deque()
    queue.append(start)
    dist[start] = 0
    while queue:
        now = queue.popleft()
        for vertex in adj[now]:
            if dist[vertex] == float('inf'):        # for infinity
                queue.append(vertex)
                dist[vertex] = dist[now] + 1
    return dist[end]

if __name__ == '__main__':
    # TEST 2
    n_vertices, n_edges = map(int, input().split())
    adj_list = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    u, v = map(int, input().split())
    distance = BFS(n_vertices, adj_list, u, v)
    if distance == float('inf'):        # for infinity
        print(-1)
    else:
        print(distance)


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
    # s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    # print(distance(adj, s, t))
