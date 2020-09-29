#Uses python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)   # new thread size which will get stack


def explore(vertex, graph, visited):
    result = 0
    #write your code here
    return result

def explore_clock(vertex, graph, visited, post):
    pass

def DFS(n, graph):
    pass

def number_of_SCC(n, reverse_graph, graph):
    pass

def main():
    pass

    
if __name__ == '__main__':
    # TEST 2
    threading.Thread(target=main).start()

    # TEST 1
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    # print(number_of_strongly_connected_components(adj))
