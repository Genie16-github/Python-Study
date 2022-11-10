# 수열 추측하기
import sys
input = sys.stdin.readline


def check_sum(arr):
    global check
    if len(arr) == 1:
        if arr[0] == F:
            check = True
        return
    else:
        tmp = []
        for i in range(len(arr)-1):
            tmp.append(arr[i] + arr[i+1])
        check_sum(tmp)
    return check


def dfs(x):
    if x == N:
        # print(res)
        if check_sum(res):
            for x in res:
                print(x, end=' ')
            sys.exit(0)
    else:
        for i in range(1, N+1):
            if not ch[i]:
                ch[i] = True
                res[x] = i
                dfs(x+1)
                ch[i] = False


if __name__ == "__main__":
    N, F = map(int, input().split())
    ch = [False] * (N+1)
    check = False
    res = [0] * N
    dfs(0)
