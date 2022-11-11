# [S1]케빈 베이컨의 6단계 법칙
import sys
from collections import deque
input = sys.stdin.readline


def bfs(v):
    q = deque([v])
    visited[v] = 1

    while q:
        target = q.popleft()

        # 친구 관계를 확인하고 탐색하지 않은 친구라면 탐색한다.
        for k in graph[target]:
            if not visited[k]:
                # 탐색하기 위한 횟수를 체크한다.
                visited[k] = visited[target] + 1
                q.append(k)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 케빈 베이컨의 수를 담는 리스트
res = []

# 반복문을 통해 모든 친구를 탐색한다.
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    bfs(i)
    res.append(sum(visited))

# 가장 작은 케빈 베이컨의 수를 가지고 있는 사람의 인덱스 + 1 을 해주어 출력한다.
print(res.index(min(res)) + 1)
