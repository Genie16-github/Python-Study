import sys
input = sys.stdin.readline


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


# 유니온 파인드
n = int(input())
m = int(input())
parents = [i for i in range(n)]
for i in range(n):
    link = list(map(int, input().split()))
    for j in range(n):
        if link[j] == 1:
            union(i, j)

# 경로 체크
parents = [0] + parents
path = list(map(int, input().split()))
start = parents[path[0]]
for i in range(1, m):
    if parents[path[i]] != start:
        print("NO")
        break
else:
    print("YES")