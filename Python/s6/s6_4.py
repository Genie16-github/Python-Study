# 합이 같은 부분집합(DFS : 아마존 인터뷰)
def dfs(v):
    if v == N:
        global res
        sum1 = 0
        for i in range(N):
            if ch[i] == 1:
                sum1 += nums[i]
        if sum1 > total // 2:
            return
        if sum1 == (total - sum1):
            res = True
            return
    else:
        ch[v] = 1
        dfs(v+1)
        ch[v] = 0
        dfs(v+1)


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    ch = [0] * N
    total = sum(nums)
    res = False
    dfs(0)

    print("YES") if res else print("NO")
