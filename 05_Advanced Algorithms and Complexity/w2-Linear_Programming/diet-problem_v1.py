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
    while pivot.row < len(a) and (used_rows[pivot.row] or a[pivot.row][pivot.col] == 0):
        pivot.row += 1
    if pivot.row == len(a):
        return False
    else:
        return pivot


# swap row to top of non-pivot rows
def swap_lines(a, b, used_rows, pivot):
    a[pivot.col], a[pivot.row] = a[pivot.row], a[pivot.col]
    b[pivot.col], b[pivot.row] = b[pivot.row], b[pivot.col]
    used_rows[pivot.col], used_rows[pivot.row] = used_rows[pivot.row], used_rows[pivot.col]
    pivot.row = pivot.col


def process_pivot_element(a, b, pivot, used_rows):
    scale = a[pivot.row][pivot.col]
    if scale != 1:
        for i in range(len(a)):
            a[pivot.row][i] /= scale
        b[pivot.row] /= scale
    for i in range(len(a)):
        if i != pivot.row:
            multiple = a[i][pivot.col]
            for j in range(len(a)):
                a[i][j] -= a[pivot.row][j] * multiple
            b[i] -= b[pivot.row] * multiple
        used_rows[pivot.row] = True


def find_subsets(n, m):
    lst = list(range(n + m + 1))
    subsets = list(map(set, itertools.combinations(lst, m)))


def gaussian_elimination(subset, A, B):
    # make equation
    a = []
    b = []
    for i in subset:
        a.append(copy.deepcopy(A[i]))


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
    sub = find_subsets(n_equations, n_variables)
    # print('subsets', sub)

    solve(sub, A, B, pleasure, n_variables)
    exit(0)
