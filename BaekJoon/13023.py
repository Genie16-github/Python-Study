# [G5]ABCDE
def dfs(depth, x):
    global result
    if depth == 4:
        result = 1
        return

    for i in link[x]:
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i)
            visited[i] = False


n, m = map(int, input().split())

link = [[] for _ in range(n)]
visited = [False] * n
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

for i in range(n):
    visited[i] = True
    dfs(0, i)
    visited[i] = False
    if result:
        break

if result:
    print(1)
else:
    print(0)
