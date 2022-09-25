# [S4]어두운 굴다리
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
x = list(map(int, input().split()))
height, last_light = x[0], x[0]

for i in range(1, m):
    tmp = abs(last_light - x[i])

    if tmp % 2 == 0:
        tmp = tmp // 2
    else:
        tmp = (tmp // 2) + 1
    height = max(height, tmp)
    last_light = x[i]

height = max(height, abs(n-x[m-1]))

print(height)
