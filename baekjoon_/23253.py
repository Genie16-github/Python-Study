import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = True

for _ in range(m):
    i = int(input())
    arr = list(map(int, input().split()))
    for j in range(i-1):
        if arr[j] < arr[j+1]:
            k = False
            break
    if not k:
        break

if k:
    print('Yes')
else:
    print('No')
