# [S1]맥주 마시면서 걸어가기
from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    q = deque()
    xy = [list(map(int, input().split())) for _ in range(n+2)]
    q.append([xy[0][0], xy[0][1]])
    visited = [0] * (n+2)
    res = 0

    while len(q) != 0:
        start = q[0]
        q.popleft()
        if xy[n+1][0] == start[0] and xy[n+1][1] == start[1]:
            res = 1
            break

        for i in range(n+1):
            if visited[i] == 0 and (abs(start[0] - xy[i+1][0]) + abs(start[1] - xy[i+1][1]) <= 1000):
                visited[i] = 1
                q.append([xy[i+1][0], xy[i+1][1]])

    if res:
        print("happy")
    else:
        print("sad")
