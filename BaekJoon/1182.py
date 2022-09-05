# [S2]부분수열의 합
import sys
input = sys.stdin.readline

def combi(depth, start):
    global cnt
    if depth == r:
        if sum(isSelected) == s:
            cnt += 1
        return

    for i in range(start, n):
        isSelected[depth] = arr[i]
        combi(depth+1, i+1)


n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for r in range(1, n+1):
    isSelected = [0] * r
    combi(0, 0)

print(cnt)


