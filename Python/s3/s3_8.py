# 곶감(모래시계)
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if b == 0:
        for _ in range(c):
            graph[a-1].append(graph[a-1].pop(0))
    else:
        for _ in range(c):
            graph[a-1].insert(0, graph[a-1].pop())

s, e = 0, N
cnt = 0
for i in range(N):
    for j in range(s, e):
        cnt += graph[i][j]
    if i < N//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(cnt)
