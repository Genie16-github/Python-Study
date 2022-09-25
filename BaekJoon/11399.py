# [S4]ATM
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

total = 0
res = []
for i in data:
    total += i
    res.append(total)

print(sum(res))