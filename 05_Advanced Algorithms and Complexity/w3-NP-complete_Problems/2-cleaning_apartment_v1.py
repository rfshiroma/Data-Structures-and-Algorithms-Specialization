# python3

import itertools


n, m = list(map(int, stdin.readline().split()))
edges = [list(map(int, input().split())) for i in range(m)]

V = []
for i in range(1, n + 1):
    # each node must appear in the path
    Xij = list(j for j in range((i-1) * n + 1, i * n + 1))
    V.append(Xij)
    # each node must appear once in the path
    lst = list(-x for x in Xij)
    subsets = list(map(list, itertools.combinations(lst, 2)))
    A += subsets

E = []
for i in range(1, n + 1):
    # every position in the path must be occupied
    pos = list(k for k in range(i, n * n + i, n))
    E.append(pos)
    # every position in the path can only have one node
    lst = list(-x for x in pos)
    subsets = list(map(list, itertools.combinations(lst, 2)))
    E += subsets


# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
# def printEquisatisfiableSatFormula():
#     print("3 2")
#     print("1 2 0")
#     print("-1 -2 0")
#     print("1 -2 0")
#
# printEquisatisfiableSatFormula()
