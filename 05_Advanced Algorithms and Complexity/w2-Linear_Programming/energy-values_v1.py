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
