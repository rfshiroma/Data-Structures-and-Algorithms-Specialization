#Uses python3
# Good job! (Max time used: 2.07/10.00, max memory used: 12132352/536870912.)

import sys
from collections import namedtuple

# Given an directed graph with possibly negative edges weights and with n vertices and m edges, check whether it contains a cycle of negative weight. Output 1 for yes, otherwise 0.
# Edge = namedtuple('Edge', ['start', 'end', 'weight'])
def bellmanFord(n, graph):
    # dist = [float('inf')] * (n+1)
    dist = [1001] * (n+1)
    dist[1] = 0
    prev = [None] * (n+1)
    negative_nodes = []
    for i in range(n):
        for u, v, w in graph:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                if i == n - 1:
                    negative_nodes.append(v)
    if not negative_nodes:
        return 0
    else:
        return 1


if __name__ == '__main__':
    # TEST 2
    n_vertices, n_edges = map(int, input().split())
    edges = []
    for i in range(n_edges):
        a, b, w = map(int, input().split())
        edges.append((a, b, w))  # (start, end, weight)
    negative_cycle = bellmanFord(n_vertices, edges)
    print(negative_cycle)

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
    # print(negative_cycle(adj, cost))
