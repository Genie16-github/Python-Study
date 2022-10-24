# [S2]좌표 압축
import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
x_idx = list(sorted(set(x)))
x_idx = {x_idx[i]: i for i in range(len(x_idx))}

print(*[x_idx[i] for i in x])
