#Uses python3
# Good job! (Max time used: 0.01/5.00, max memory used: 9412608/536870912.)


import sys


def explore(edges, vertex, visited, stack, is_dag):
    visited[vertex] = True
    stack.append(vertex)
    for v in edges[vertex]:
        if v in stack:
            is_dag[0] = False
        if not visited[v]:
            explore(edges, v, visited, stack, is_dag)           # recursive call
    stack.pop()

def is_DAG(edges, visited, n):
    is_dag = [True]
    stack = []
    for i in range(1, n+1):
        if not visited[i]:
            explore(edges, i, visited, stack, is_dag)           # recursive call
            if not is_dag[0]:
                return False
    return True

if __name__ == '__main__':
    # TEST 2
    n_vertices, n_edges = map(int, input().split())
    edges = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        a, b = map(int, input().split())
        edges[a].append(b)
    visited = [False] * (n_vertices + 1)
    check = is_DAG(edges, visited, n_vertices)
    if check:
        print(0)
    else:
        print(1)

    # TEST 1
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
