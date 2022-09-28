# [S4]로프
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
res = 0
for i in range(n):
    tmp = data[i] * (n-i)
    res = max(tmp, res)

print(res)