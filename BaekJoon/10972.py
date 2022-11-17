# [S3]다음 순열
import sys
sys.setrecursionlimit(10**6)


def dfs(v):
    global res
    if v == n:
        if res:
            print(*isSelected)
            res = False
            return
        if isSelected == nums:
            res = True

    else:
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = 1
                isSelected[v] = i+1
                dfs(v+1)
                visited[i] = 0


n = int(input())
nums = list(map(int, input().split()))
visited = [0]*n
isSelected = [0]*n
res = False
dfs(0)
if res:
    print(-1)