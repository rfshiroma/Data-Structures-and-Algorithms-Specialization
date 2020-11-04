# python3

class Node:
    def __init__(self, i):
        self.r = 3 * i - 2
        self.g = 3 * i - 1
        self.b = 3 * i


n_vertices, n_edges = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

V = []
for i in range(1, n_vertices + 1):
    node = Node(i)
    V.append()
    V.append()
    V.append()
    V.append()


E = []
for a, b in edges:
    u = Node(a)
    v = Node(b)
    E.append()
    E.append()
    E.append()


n_clauses = len(V) + len(E)
n_variables = n_vertices * 3
print(n_clauses, n_variables)


for clause in V:
    for i in clause:
        print(i, end= ' ')
    print(0)

for clause in E:
    for i in clause:
        print(i, end=' ')
    print(0)



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
