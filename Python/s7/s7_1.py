# 최대 점수 구하기
import sys
input = sys.stdin.readline


def dfs(v, total, time):
    global res
    if time > m:
        return
    if v == n:
        if res < total:
            res = total
    else:
        dfs(v+1, total+pr[v][0], time+pr[v][1])
        dfs(v+1, total, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    pr = [list(map(int, input().split())) for _ in range(n)]
    res = -2147000000
    dfs(0, 0, 0)
    print(res)


"""
def dfs(v, total, time, ch):
    global res
    if ch == 1:
        if res < total:
            res = total
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                tmp = time + pr[i][1]
                if tmp > m:
                    dfs(v+1, total, tmp, 1)
                else:
                    dfs(v+1, total + pr[i][0], tmp, 0)
                visited[i] = False


if __name__ == "__main__":
    n, m = map(int, input().split())
    pr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    res = -2147000000
    dfs(0, 0, 0, 0)
    print(res)
"""
