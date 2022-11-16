# [모의 SW 역량테스트] 보호 필름
import sys
sys.setrecursionlimit(10**6)


def dfs(v, cnt):
    global res
    if res < cnt:
        return
    if v == d:
        if check(board):
            if res > cnt:
                res = cnt
        return
    else:
        dfs(v+1, cnt)

        tmp = board[v]
        board[v] = [1]*w
        dfs(v+1, cnt+1)
        board[v] = [0]*w
        dfs(v+1, cnt+1)
        board[v] = tmp


def check(graph):
    for i in range(w):
        tmp = 1
        std = graph[0][i]
        for j in range(1, d):
            if std == graph[j][i]:
                tmp += 1
            else:
                tmp = 1
                std = graph[j][i]
            if tmp == k:
                break
        else:
            return False
    return True


t = int(input())
for tc in range(1, t+1):
    res = 2147000000
    d, w, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(d)]
    if check(board):
        print('#%d 0' % tc)
    else:
        dfs(0, 0)
        print('#%d %d' % (tc, res))
