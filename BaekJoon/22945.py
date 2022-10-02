# [G4]팀 빌딩
import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

l, r = 0, n-1
res = 0

while l+1 < r:
    res = max(res, (r-l-1) * min(x[l], x[r]))
    if x[l] < x[r]:
        l += 1
    else:
        r -= 1

print(res)
