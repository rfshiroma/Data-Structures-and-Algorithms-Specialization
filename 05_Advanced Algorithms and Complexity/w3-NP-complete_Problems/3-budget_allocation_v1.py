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

    # clauses which make inequelities unsatisfiable
    elif len(C) == 1:
        for u in lst1:
            if A[i][C[0]] * u > b[i]:
                if u == 0:
                    clauses.append([C[0] + 1])
                else:
                    clauses.append([- C[0] - 1])
    elif len(C) == 2:
        for u, v in lst2:
            if A[i][C[0]] * u + 


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
