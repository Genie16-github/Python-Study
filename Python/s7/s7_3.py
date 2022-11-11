# 양팔저울
import sys
input = sys.stdin.readline


def dfs(v, total):
    if v == n:
        if total > 0 and total in range(1, sum(w)+1):
            ch[total] += 1
    else:
        dfs(v+1, total+w[v])
        dfs(v+1, total)
        dfs(v+1, total-w[v])


n = int(input())
w = list(map(int, input().split()))
ch = [0] * (sum(w)+1)
cnt = 0
dfs(0, 0)
for x in ch:
    if x == 0:
        cnt += 1
print(cnt-1)