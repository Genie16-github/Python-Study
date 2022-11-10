# 순열 구하기
import sys
input = sys.stdin.readline


def dfs(x):
    global cnt
    if x == M:
        for x in res:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, N+1):
            if not visited[i]:
                visited[i] = True
                res[x] = i
                dfs(x+1)
                visited[i] = False


if __name__ == "__main__":
    N, M = map(int, input().split())
    visited = [False] * (N+1)
    res = [0] * M
    cnt = 0
    dfs(0)
    print(cnt)