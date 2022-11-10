# [S1]RGB 거리
import sys
input = sys.stdin.readline


def dfs(idx, x, total):
    global res
    if total > res:
        return
    if idx == N+1:
        if res > total:
            res = total
    else:
        for i in range(3):
            if i == x:
                continue
            else:
                dfs(idx+1, i, total + color[idx][i])


if __name__ == "__main__":
    N = int(input())
    color = [[0]*3] + [list(map(int, input().split())) for _ in range(N)]
    res = 2147000000
    dfs(1, -1, 0)
    print(res)