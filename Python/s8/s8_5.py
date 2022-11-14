# 가장 높은 탑 쌓기
n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
info.sort(reverse=True)
info.insert(0, [0, 0, 0])
dp = [0] * (n+1)
dp[1] = info[1][1]
res = info[1][1]

for i in range(2, n+1):
    max_h = 0
    for j in range(i-1, 0, -1):
        if info[i][2] < info[j][2] and dp[j] > max_h:
            max_h = dp[j]
    dp[i] = max_h + info[i][1]
    res = max(res, dp[i])

print(res)