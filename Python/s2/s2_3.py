# K번째 큰 수
import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # N(3<=N<=100), K(1<=K<=50)
nums = list(map(int, input().split()))
res = set()

for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            res.add(nums[a] + nums[b] + nums[c])

res = sorted(list(res), reverse=True)
print(res[K-1])
