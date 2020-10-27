from collections import deque

def has_path(Gf, path):
    n = len(Gf)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])
    while queue:
        temp = queue.popleft()
        if temp == n - 1:
            return True
        for i in range(n):
            if not visited[i] and Gf[temp][i] > 0:
                queue.append(i)
                visited[i] = True
                path[i] = temp
    return visited[n-1]

def maxflow(Gf):
    pass

if __name__ == '__main__':
    pass
