# [S4]제로
import sys
input = sys.stdin.readline

res = []
for _ in range(int(input())):
    data = int(input())
    res.append(data) if data else res.pop()

print(sum(res))