# 동전 바꿔주기
import sys
input = sys.stdin.readline


def dfs(v, total):
    global cnt
    if total > t:
        return
    if v == k:
        if total == t:
            cnt += 1
    else:
        for n in range(visited[v]+1):
            dfs(v+1, total + coin[v]*n)


if __name__ == "__main__":
    t = int(input())
    k = int(input())
    visited = [0] * k
    cnt = 0
    coin = []
    for i in range(k):
        a, b = map(int, input().split())
        coin.append(a)
        visited[i] = b
    dfs(0, 0)
    print(cnt)