# python3

import itertools
import copy

EPS = 1e-18
PRECISION = 18

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def select_pivot_element(pivot, a, used_row):
    pass


# swap row to top of non-pivot rows
def swap_lines(a, b, used_rows, pivot):
    pass


def process_pivot_element(a, b, pivot, used_rows):
    pass


def find_subsets(n, m):
    pass


def gaussian_elimination(subset, A, B):
    pass


def check_solution(solution, A, B, m):
    pass

def solve(subsets, A, B, pleasure, m):
    pass


if __name__ == '__main__':
    n_equations, n_variables = map(int, input().split())
    A = []
    for i in range(n_equations):
        A.append(list(map(int, input().split())))
    B = list(map(int, input().split()))
    pleasure = list(map(int, input().split()))
    for i in range(n_variables):
        lst = [0] * n_variables
        lst[i] = - 1
        A.append(lst)
        B.append(0)
    A.append([1] * n_variables)
    B.append(1000000001)
    # print('A', A, 'B', B)
    sub = FindSubsets(n_equations, n_variables)
    # print('subsets', sub)

    solve(sub, A, B, pleasure, n_variables)
    exit(0)
