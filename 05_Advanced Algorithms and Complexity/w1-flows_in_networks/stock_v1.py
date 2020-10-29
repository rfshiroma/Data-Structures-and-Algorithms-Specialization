# python3

from colletions import deque

def DAG(n, stock):
    pass

def make_network(n, adj):
    pass

def has_path(Gf, path):
    pass

def maxflow(Gf):
    pass

if __name__ == '__main__':
    n, m = map(int, input().split())
    stock_data = [list(map(int, input().split())) for _ in range(n)]
    adj_matrix = DAG(n, stock_data)
    graph = make_network(n, adj_matrix)
    max_flow = maxflow(graph)
    min_charts = n - max_flow
    print(min_charts)
