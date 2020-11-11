# python3

from itertools import permutations
from itertools import combinations
from collections import deque

INF = 10**9


def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]  # adjacent matrix
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph


def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))


def optimal_path(graph):
    pass


if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
