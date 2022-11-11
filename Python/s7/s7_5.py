# 동전 분배하기
import sys
input = sys.stdin.readline


def dfs(v):
    global res
    if v == n:
        tmp = max(money) - min(money)
        if res > tmp:
            tmp2 = set(money)
            if len(tmp2) == 3:
                res = tmp

    else:
        for i in range(3):
            money[i] += coin[v]
            dfs(v+1)
            money[i] -= coin[v]


if __name__ == "__main__":
    n = int(input())
    coin = [int(input()) for _ in range(n)]
    res = 2147000000
    money = [0] * 3
    dfs(0)
    print(res)