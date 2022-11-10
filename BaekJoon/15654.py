# [S3]N과 M(5)
import sys
input = sys.stdin.readline


def dfs(x):
    if x == M:
        for x in res:
            print(x, end=' ')
        print()
    else:
        for idx, i in enumerate(nums):
            if not ch[idx]:
                ch[idx] = True
                res[x] = i
                dfs(x+1)
                ch[idx] = False


if __name__ == "__main__":
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    ch = [False] * N
    res = [0] * M
    dfs(0)