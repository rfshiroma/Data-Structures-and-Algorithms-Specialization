# python3


# from collections import deque

# A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V such that every edge (u, v) either connects a vertex from U to V, or a vertex from V to U. In other words, for every edge (u, v), either u belongs to U and v to V, or u belongs to V and v to U. We can also say that there is no edge that connects vertices of same set.

def check_Bipartite(graph):
    queue = []
    visited = [False] * len(graph)

    # the value "-1" of color is assigned to graph vertex
    color = [-1] * len(graph)

    def bfs():
        while queue:
            u = queue.pop(0)    # FIFO (First In First Out)
            visited[u] = True

            for neighbour in graph[u]:
                if neighbour == u:
                    return False

                if color[neighbour] == -1:      # not visited neighbour
                    color[neighbour] = 1 - color[u]
                    queue.append(neighbour)

                elif color[neighbour] == color[u]:
                    return False
        return True


    for i in range(len(graph)):
        if not visited[i]:
            queue.append(i)
            color[i] = 0
            if bfs() is False:
                return 0
    return 1



if __name__ == '__main__':
    # TEST 2
    adj_map0 = {0: [1,3], 1: [0,2], 2: [1,3], 3: [0,2]}
    print(check_Bipartite(adj_map0))
    # adj_map1 = {0: [1,2], 1: [4,1], 2: [2,3], 3: [3,1]}
    # print(check_Bipartite(adj_map1))
    # adj_map2 = {0: [5,2], 1: [4,2], 2: [3,4], 3: [1,4]}
    # print(check_Bipartite(adj_map2))

    # TEST 1
    # n_vertices, n_edges = map(int, input().split())
    # adjacency_list = [[] for _ in range(n_vertices + 1)]
    # for i in range(n_edges):
    #     a, b = map(int, input().split())
    #     adjacency_list[a].append(b)
    #     adjacency_list[b].append(a)
    # is_bipartite = is_Bipartite(n_vertices, adjacency_list)
    # print(is_bipartite)
