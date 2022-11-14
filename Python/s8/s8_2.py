# 네트워크 선 자르기
def dfs(v):
    if dp[v] > 0:
        return dp[v]
    if v == 1 or v == 2:
        return v
    else:
        dp[v] = dfs(v-1) + dfs(v-2)
        return dp[v]


n = int(input())
dp = [0] * (n+1)
print(dfs(n))