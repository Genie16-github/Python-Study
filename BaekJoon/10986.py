# [G3]나머지 합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

pre_pix = [0 for i in range(m)]
pre_sum = 0

pre_pix[0] = 1

for i in range(n):
    pre_sum += data[i]
    pre_pix[pre_sum % m] += 1

res = 0
for i in pre_pix:
    res += i * (i - 1) // 2

print(res)