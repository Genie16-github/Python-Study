# 격자판 최대합
max_sum = -2147000000
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):  # 각 행, 열의 합 비교
    sum1 = sum2 = 0
    for j in range(N):
        sum1 += graph[i][j]  # 행의 합
        sum2 += graph[j][i]  # 열의 합
    if sum1 > max_sum:
        max_sum = sum1
    if sum2 > max_sum:
        max_sum = sum2

sum1 = sum2 = 0
for i in range(N):  # 두 대각선 합 비교
    sum1 += graph[i][i]
    sum2 += graph[i][N-1-i]
    if sum1 > max_sum:
        max_sum = sum1
    if sum2 > max_sum:
        max_sum = sum2

print(max_sum)
