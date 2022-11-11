# 휴가(삼성 SW 역량평가 기출문제 : DFS 활용)
import sys
input = sys.stdin.readline


def dfs(v, total):
    global res
    if v > n+1:
        return
    if v == n+1:
        if total > res:
            res = total
    else:
        dfs(v+tp[v][0], total+tp[v][1])
        dfs(v+1, total)


if __name__ == "__main__":
    n = int(input())
    tp = [[0]*2] + [list(map(int, input().split())) for _ in range(n)]
    # print(tp)
    res = -2147000000
    dfs(1, 0)
    print(res)