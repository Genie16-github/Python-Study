# 최대 부분 증가수열
n = int(input())
nums = list(map(int, input().split()))
dp = [0] * (n+1)
nums.insert(0, 0)
dp[1] = 1
res = 0
for i in range(2, n+1):
    tmp = 0
    for j in range(i-1, 0, -1):
        if nums[i] > nums[j] and dp[j] > tmp:
            tmp = dp[j]
    dp[i] = tmp+1
    if dp[i] > res:
        res = dp[i]

print(res)