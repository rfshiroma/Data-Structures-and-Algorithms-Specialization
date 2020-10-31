# python3


EPS = 1e-6
PRECISION = 6

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def read_data():
        size = int(input())
        a = []
        b = []
        for _ in range(size):
            line = list(map(float, input().split()))
            a.append(line[:size])
            b.append(line[size])
        return Equation(a, b)

def select_pivot_element(pivot, a, used_rows):
    pass

# swap row to top of non-pivot rows
def swap_lines(a, b, used_rows, pivot):
    pass

def process_pivot_element(a, b, pivot, used_rows):
    pass

def solve_equation(equation):
    pass

def print_column(column):
    pass

if __name__ == '__main__':
    matrix = read_data()
    solution = solve_equation(matrix)
    print_column(solution)
    exit(0)
