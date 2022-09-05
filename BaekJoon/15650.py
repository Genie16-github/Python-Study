# [S3]N과 M(2)
def combi(depth, start):
    if depth == r:
        print(*isSelected)
        return

    for i in range(start, n):
        isSelected[depth] = number[i]
        combi(depth+1, i+1)


n, r = map(int, input().split())
number = [i for i in range(1, n+1)]
isSelected = [0] * r
combi(0, 0)
