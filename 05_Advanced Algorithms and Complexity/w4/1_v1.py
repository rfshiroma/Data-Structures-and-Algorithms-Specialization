# python3

import sys
import threading

def post_order(i, graph, visited, post):
    global clock
    visited[i] = True
    for v in graph[i]:
        if not visited[v]:
            post_order(v, graph, visited, post)
    post[i] = clock
    clock += 1


def DFS(n, graph):
    global clock
    visited = [False] * (2 * n + 1)
    post = [0] * (2 * n + 1)
    for v in range(1, 2 * n + 1):
        if not visited[v]:
            post_order(v, graph, visited, post)
    post = list(enumerate(post[1:], start=1))
    post.sort(key=lambda x:x[1], reverse=True)
    post_vertex = []
    for v, order in post:
        post_vertex.append(v)
    return post_vertex


def explore(i, graph, visited, SCC, SCC_number, u):
    visited[i] = True
    SCC.append(i)
    SCC_number[i] = u
    for v in graph[i]:
        if not visited[v]:
            explore(v, graph, visited, SCC, SCC_number, u)


def find_SCCs(n, rev_graph, graph):
    global clock
    post_vertex = DFS(n, rev_graph)
    visited = [False] * (2 * n + 1)
    SCCs = []
    SCC_number = [0] * (2 * n + 1)
    u = 1
    for i in post_vertex:
        if not visited[i]:
            SCC = []
            explore(i, graph, visited, SCC, SCC_number, u)
            SCCs.append(SCC)
            u += 1
    return SCCs, SCC_number


def two_SAT(n, rev_graph, graph):
    SCCs, SCC_number = find_SCCs(n, rev_graph, graph)
    # print(SCCs, SCC_number)
    for i in range(1, n + 1):
        if SCC_number[i] == SCC_number[i + n]:
            return False
    solution =[[] for _ in range(2 * n + 1)]
    assigned = [False] * (2 * n + 1)
    for SCC in SCCs:
        for v in SCC:
            if not assigned[v]:
                assigned[v] = True
                solution[v] = 1
                if v > n:
                    solution[v - n] = 0
                    assigned[v - n] = True
                else:
                    solution[v + n] = 0
                    assigned[v + n] = True
    return solution


clock = 1
def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(2 * n + 1)]
    rev_edges = [[] for _ in range(2 * n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        if a > 0 and b > 0:
            edges[a + n].append(b)
            edges[b + n].append(a)
            rev_edges[b].append(a + n)
            rev_edges[a].append(b + n)
        elif a < 0 and b < 0:
            edges[-a].apend(-b + n)
            edges[-b].append(-a + n)
            rev_edges[-b + n].append(-a)
            rev_edges[-a + n].append(-b)
        elif a < 0 and b > 0:
            edges[-a].append(b)
            edges[b + n].append(-a + n)
            rev_edges[b].append(-a)
            rev_edges[-a + n].append(b + n)
        elif a > 0 and b < 0:
            edges[a + n].append(-b + n)
            edges[-b].append(a)
            rev_edges[-b + n].append(a + n)
            rev_edges[a].append(-b)
    # print(edges)
    # print(rev_edges)
    result = two_SAT(n, rev_edges, edges)
    if not result:
        print('UNSATISFIABLE')
    else:
        print('SATISFIABLE')
        for i in range(1, n + 1):
            if result[i] > 0:
                print(i, end=' ')
            else:
                print(-i, end=' ')

# This is to avoid stack overflow issues
threading.Thread(target=main).start()
