# 조합구하기(DFS)
import sys
input = sys.stdin.readline


def dfs(idx, f):
    global cnt
    if idx == M:
        for x in res:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for i in range(f, N+1):
            res[idx] = i
            dfs(idx+1, i+1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    res = [0] * M
    cnt = 0
    dfs(0, 1)
    print(cnt)
