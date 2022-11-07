# 격자판 회문수
graph = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(7):
    for j in range(3):
        if all(graph[i][j+k] == graph[i][j+4-k] for k in range(2)):
            cnt += 1
        if all(graph[j+k][i] == graph[j+4-k][i] for k in range(2)):
            cnt += 1

print(cnt)
