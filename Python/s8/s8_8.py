# 동전 교환
n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dp = [501] * (m+1)
dp[0] = 0

for i in coin:
    for j in range(i, m+1):
        dp[j] = min(dp[j], dp[j-i] + 1)

print(dp[m])
