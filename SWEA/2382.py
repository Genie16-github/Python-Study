# [모의 SW 역량테스트] 미생물 격리
import math
from collections import deque


def bfs():
    global res
    visited = [[[0, 0]]*n for _ in range(n)]
    graph = [[[0, 0]]*n for _ in range(n)]
    res = 0
    while q:
        x, y, cnt, dirt = q.popleft()
        nx = x + dx[dirt]
        ny = y + dy[dirt]
        if (0 <= nx < n) and (0 <= ny < n):
            # 약품이 칠해진 곳
            if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
                tmp = math.trunc(cnt/2)
                dirt = r_dirt[dirt]
                graph[nx][ny] = [tmp, dirt]
            else:
                # 방문 처리가 안 되어있다면 값 넣고 방문 처리
                if visited[nx][ny] == [0, 0]:
                    graph[nx][ny] = [cnt, dirt]
                    visited[nx][ny] = [cnt, dirt]
                # 방문 처리가 돼있다면 개체 수 합치기
                else:
                    if visited[nx][ny][0] > cnt:
                        graph[nx][ny][0] += cnt
                    else:
                        graph[nx][ny][0] += cnt
                        visited[nx][ny] = [cnt, dirt]
                        graph[nx][ny][1] = dirt
    for i in range(n):
        for j in range(n):
            if graph[i][j] != [0, 0] and graph[i][j][0] != 0:
                q.append((i, j, graph[i][j][0], graph[i][j][1]))
                res += graph[i][j][0]


dx = [0, -1, 1, 0, 0]  # 상하좌우
dy = [0, 0, 0, -1, 1]
r_dirt = [0, 2, 1, 4, 3]

t = int(input())
for tc in range(1, t+1):
    q = deque()
    res = 0
    # n : 한 변에 있는 셀의 개수. m : 격리시간. k : 미생물 군집의 개수
    n, m, k = map(int, input().split())
    for _ in range(k):
        # h : 세로위치. w : 가로위치. m_cnt : 미생물 수. move : 이동 방향
        h, w, m_cnt, move = map(int, input().split())
        q.append((h, w, m_cnt, move))

    for _ in range(m):  # 시간만큼 실행
        bfs()
    print('#%d %d' % (tc, res))

