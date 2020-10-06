#Uses python3
# Good job! (Max time used: 1.96/10.00, max memory used: 13836288/536870912.)

import sys
from collections import deque

# Given an indirected graph with possibly negative edge weights and with n vertices and m edges as well as its vertex s, compute the length of shortest paths from s to all other vertices of the graph.
def bellFord(n, graph, adj, s):
    dist = [float('inf')] * (n+1)
    dist[s] = 0
    prev = [None] * (n+1)
    negative_nodes = deque()
    for i in range(n):
        for u, v, w in graph:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                if i == n - 1:
                    negative_nodes.append(v)

    visited = [False] * (n+1)
    while negative_nodes:
        u = negative_nodes.popleft()
        visited[u] = True
        dist[u] = '-' # nodes reachable from negative cycle
        for v in adj[u]:
            if not visited[v]:
                negative_nodes.append(v)
    return dist


if __name__ == '__main__':
    # TEST 2
    n_vertices, n_edges = map(int, input().split())
    edges = []
    adj_list = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        a, b, w = map(int, input().split())
        edges.append((a, b, w))     # (start, end, weight)
        adj_list[a].append(b)       # start: [end, weight]
    start = int(input())
    distance = bellFord(n_vertices, edges, adj_list, start)
    for dist in distance[1:]:
        if dist == float('inf'):
            print('*')  # there is no path from a to b
        else:
            print(dist)

    # TEST 1
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    # data = data[3 * m:]
    # adj = [[] for _ in range(n)]
    # cost = [[] for _ in range(n)]
    # for ((a, b), w) in edges:
    #     adj[a - 1].append(b - 1)
    #     cost[a - 1].append(w)
    # s = data[0]
    # s -= 1
    # distance = [10**19] * n
    # reachable = [0] * n
    # shortest = [1] * n
    # shortet_paths(adj, cost, s, distance, reachable, shortest)
    # for x in range(n):
    #     if reachable[x] == 0:
    #         print('*')
    #     elif shortest[x] == 0:
    #         print('-')
    #     else:
    #         print(distance[x])
