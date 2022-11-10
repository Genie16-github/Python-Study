# 중복순열 구하기
def dfs(x):
    global cnt
    if x == M:
        for x in res:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, N+1):
            res[x] = i
            dfs(x+1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    res = [0] * M
    cnt = 0
    dfs(0)
    print(cnt)