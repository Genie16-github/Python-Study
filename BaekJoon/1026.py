# [S4]보물
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = 0

A.sort()
B.sort(reverse=True)

for x in range(n):
    res += A[x] * B[x]

print(res)
