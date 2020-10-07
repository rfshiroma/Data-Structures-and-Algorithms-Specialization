#Uses python3
# Good job! (Max time used: 0.05/10.00, max memory used: 10547200/536870912.)

import sys
import math

# In this problem, the goal is to build roads between some pairs of the given cities such that there is a path between any two cities and the total length of the roads is minimized.

# Kruskal's algorithm: repeatedly add the next lightest edge if this does not produce a cycle.

class MinimumLength:
    def __init__(self, n, edges):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.edges = edges

    def union(self, i, j):
        i_parent = self.find(i)
        j_parent = self.find(j)
        if i_parent == j_parent:
            return
        else:
            if self.rank[i_parent] > self.rank[j_parent]:
                self.parent[j_parent] = i_parent
            else:
                self.parent[i_parent] = j_parent
                if self.rank[i_parent] == self.rank[j_parent]:
                    self.rank[j_parent] += 1


    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def kruskal(self):
        dist = 0
        self.edges.sort(key=lambda i: i[2])  # sort edges by weight
        for u, v, w in edges:
            # check whether the current edge {u,v} produces a cycle, we check whether u and v belong to the same set
            if self.find(u) != self.find(v):
                dist += w
                self.union(u, v)
        return dist


if __name__ == '__main__':
    # TEST 2
    n_vertices = int(input())
    points = [None] * n_vertices    # 0-based index
    for i in range(n_vertices):
        a, b = map(int, input().split())
        points[i] = (a, b)
    edges = []                      # (start, end, weight)

    for i in range(n_vertices):
        (x0, y0) = points[i]
        for j in range(i + 1, n_vertices):
            (x, y) = points[j]
            distance = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
            edges.append((i, j, distance))
    graph = MinimumLength(n_vertices, edges)
    min_length = graph.kruskal()
    print("{0:.9f}".format(min_length))


    # TEST 1
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # x = data[1::2]
    # y = data[2::2]
    # print("{0:.9f}".format(minimum_distance(x, y)))
