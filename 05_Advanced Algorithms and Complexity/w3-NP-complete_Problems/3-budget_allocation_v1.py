# python3

import itertools


n, m = list(map(int, input().split()))
A = []
for i in range(n):
    A += [list(map(int, input().split()))]
b = list(map(int, input().split()))

lst1 = [0, 1]
lst2 = [[0, 0], [1, 0], [0, 1], [1, 1]]
lst3 = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]]

clauses =[]
for i in range(n):
    # find non-zero coefficients
    C = [] # non-zero coefficients
    for j in range(m):
        if A[i][j] != 0:
            C.append(j)
    if len(C) == 0:
        if b[i] < 0:
            clauses = [[1], [-1]]
            break
        else:
            continue


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
