# K번째 약수
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
i = 1
res = []
while i < n+1:
    if n % i == 0:
        res.append(i)
    i += 1

print(res[k-1]) if len(res) >= k else print(-1)

"""
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:   # n+1까지 돌아가는 와중에 탈출을 못 했다면 실행
    print(-1)
"""