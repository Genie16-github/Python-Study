# [S1]화학 제품
import sys
input = sys.stdin.readline

for T in range(int(input())):
    a, b, c = map(int, input().split())
    ab, bc, ca = map(int, input().split())
    res = 0

    for i in range(min(a, b)+1):
        if bc > ca:
            j = min(b-i, c)
            k = min(a-i, c-j)
            res = max(res, ab*i+bc*j+ca*k)
        else:
            k = min(a-i, c)
            j = min(c-k, b-i)
            res = max(res, ab*i+bc*j+ca*k)
    print(res)

