# [S3]N과 M(1)
def permu(depth):
    if depth == r:
        print(*isSelected)
        return

    for i in range(n):
        if not visited[i]:
            isSelected[depth] = number[i]
            visited[i] = 1
            permu(depth+1)
            visited[i] = 0


n, r = map(int, input().split())
number = [i for i in range(1, n+1)]
visited = [0] * (n+1)
isSelected = [0] * r

permu(0)