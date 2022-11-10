# [S2]부분수열의 합
def dfs(v):
    global cnt
    if v == N:
        total = 0
        for i in range(N):
            if ch[i] == 1:
                total += nums[i]
        if total == S and ch.count(0) != N:
            cnt += 1
    else:
        ch[v] = 1
        dfs(v+1)
        ch[v] = 0
        dfs(v+1)


if __name__ == "__main__":
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    ch = [0] * N
    cnt = 0
    dfs(0)
    print(cnt)
