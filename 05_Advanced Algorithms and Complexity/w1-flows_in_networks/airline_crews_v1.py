# python3

from collections import deque

def make_network(n, m, bip):
    pass

def has_path(Gf, path):
    pass

def maxflow(Gf, n):
    pass



if __name__ == '__main__':
    n_flights, n_crew = map(int, input().split())
    bipartite = [list(map(int, input().split())) for i in range(n_flights)]

    # compute residual Gf
    residual_graph = make_network(n_flights, n_crew, bipartite)
    matching = maxflow(residual_graph, n_flights)

    for e in matching:
        print(e, end= ' ')
