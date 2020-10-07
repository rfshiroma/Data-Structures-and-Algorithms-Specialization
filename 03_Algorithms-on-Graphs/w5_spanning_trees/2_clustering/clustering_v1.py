#Uses python3
# Good job! (Max time used: 0.81/10.00, max memory used: 10362880/536870912.)

import sys
import math

# Clustering is a fundamental problem in data mining. The goal is to partition a given set of objects into subsets (or clusters) in such a way that any two objects from the same subsets are close (or similar) to each other, while any two objects from different subsets are far apart.

# Prim's Algorithm: repeatedly attach a new vertex to the current tree by a lightest edge; use priority queue to quickly find the next lightest edge; very similar to Dijkstra's algorithm.

def distance(xi, yi, xj, yj):
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

def clustering(n, adj, weight, k):
    X = set()
    T = set()
    X.add(0)

    while len(X) != n:
        crossing = set()
        for u in X:
            for v in adj[u]:
                if v not in X:
                    crossing.add((u, v))
        edge = sorted(crossing, key=lambda e: weight[e[0]][e[1]])[0]
        T.add(edge)
        X.add(edge[1])

    T = sorted(T, key=lambda e: weight[e[0]][e[1]])

    for _ in range(k - 2):
        T.pop(len(T) - 1)

    d = T.pop(len(T) - 1)
    return weight[d[0]][d[1]]


if __name__ == '__main__':
    # TEST 2 #TODO
    # n_vertices = int(input())
    # points = [None] * n_vertices                # 0-based index
    # for i in range(n_vertices):
    #     a, b = map(int, input().split())
    #     points[i] = (a, b)
    # edges = []                                  # (start, end, weight)
    # n_subsets = int(input())
    # for i in range(n_vertices):
    #     (x0, y0) = points[i]
    #     for j in range(i + 1, n_vertices):      # range(start, stop)
    #     (x, y) = points[i]
    #     distance = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
    #     edges.append((i, j, distance))
    # graph = MinimumLength(n_vertices, edges, n_subsets)

    # TEST 1
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]

    adj = [[] for _ in range(n)]
    weight = [[0] * n for _ in range(n)]
    for i in range(n):
        adj[i] = [v for v in range(n) if v != i]
        for j in range(n):
            if i != j:
                w = distance(x[i], y[i], x[j], y[j])
                weight[i][j] = w
                weight[j][i] = w
    print("{0:.9f}".format(clustering(n, adj, weight, k)))
