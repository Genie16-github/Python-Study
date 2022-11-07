# 봉우리
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
graph = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
graph.insert(0, [0]*(N+2))
graph.append([0]*(N+2))

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if all(graph[i][j] > graph[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
