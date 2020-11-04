# python3

import itertools


n, m = list(map(int, input().split()))
A = []
for i in range(n):
  A += [list(map(int, input().split()))]
b = list(map(int, stdin.readline().split()))

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
