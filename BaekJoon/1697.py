# [S1]숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            print(visited[v])
            break
        for i in (v-1, v+1, 2*v):
            if 0 <= i < max_num and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)


max_num = 100001
visited = [0] * max_num
n, k = map(int, input().split())
bfs(n)
