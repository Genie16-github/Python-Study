# [S2]DFS와 BFS
from collections import deque
import sys
input = sys.stdin.readline


def bfs(num):
    q = deque()
    q.append(num)
    visited[num] = 1
    while q:
        num = q.popleft()
        print(num, end=" ")
        for i in range(1, n+1):
            if visited[i] == 0 and graph[num][i] == 1:
                q.append(i)
                visited[i] = 1


def dfs(num):
    visited2[num] = 1
    print(num, end=" ")
    for i in range(1, n+1):
        if visited2[i] == 0 and graph[num][i] == 1:
            dfs(i)


n, m, v = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
visited2 = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)
