# 송아지 찾기
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    while q:
        now = q.popleft()
        if now == e:
            break
        for next in (now-1, now+1, now+5):
            if 0 < next <= 10000:
                if ch[next] == 0:
                    ch[next] = 1
                    dis[next] = dis[now] + 1
                    q.append(next)


if __name__ == "__main__":
    s, e = map(int, input().split())
    ch = [0] * 10001
    dis = [0] * 10001
    q = deque()
    q.append(s)
    ch[s] = 1
    bfs()
    print(dis[e])
