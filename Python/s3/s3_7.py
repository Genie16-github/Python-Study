# 사과나무(다이아몬드)
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
s = e = N // 2

for i in range(N):
    for j in range(s, e+1):
        cnt += graph[i][j]
    if i < N//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(cnt)
