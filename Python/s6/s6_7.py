# 동전 교환
import sys
input = sys.stdin.readline


def dfs(idx, total):
    global cnt
    if idx > cnt or total > M:
        return
    if total == M:
        if idx < cnt:
            cnt = idx
    else:
        for i in range(N):
            dfs(idx+1, total + coin[i])


if __name__ == "__main__":
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    cnt = 2147000000
    coin.sort(reverse=True)
    dfs(0, 0)
    print(cnt)
