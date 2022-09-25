# [S2]한 줄로 서기
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

arr = []
for i in range(n):
    arr.insert(data[n-1-i], n-i)

for i in arr:
    print(i, end=' ')
