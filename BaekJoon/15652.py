# [S3]N과 M(4)
import sys
input = sys.stdin.readline


def dfs(x):
    if x == M:
        tmp = res[0]
        for x in res:
            if x < tmp:
                break
            else:
                tmp = x
        else:
            for x in res:
                print(x, end=' ')
            print()
    else:
        for i in range(1, N+1):
            res[x] = i
            dfs(x+1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    res = [0] * M
    dfs(0)