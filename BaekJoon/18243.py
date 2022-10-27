# [S2]Small World Network
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    check[v] = 0
    while q:
        v = q.popleft()
        for i in graph[v]:
            if check[i] == -1:
                q.append(i)
                check[i] = check[v]+1


n, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
check = [-1] * (n+1)
for _ in range(k):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ok = 1
for i in range(1, n+1):
    check = [-1] * (n+1)
    bfs(i)

    if (max(check) > 6) or (-1 in check[1:]):
        ok = 0
        break

print("Small World!" if ok else "Big World!")
