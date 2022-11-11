# 수들의 조합
import sys
input = sys.stdin.readline


def dfs(x, s):
    global cnt
    if x == K:
        if sum(res) % M == 0:
            cnt += 1

    else:
        for i in range(s, N):
            res[x] = nums[i]
            dfs(x+1, i+1)


if __name__ == "__main__":
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    res = [0] * K
    M = int(input())
    cnt = 0
    dfs(0, 0)
    print(cnt)