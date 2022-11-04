# [S3]회전하는 큐
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
K = list(map(int, input().split()))
nums = deque(i for i in range(1, N+1))
cnt, idx = 0, 0

while idx < M:
    if nums[0] == K[idx]:
        nums.popleft()
        idx += 1
    else:
        if nums.index(K[idx]) <= len(nums) // 2:
            tmp = nums.popleft()
            nums.append(tmp)
            cnt += 1
        else:
            tmp = nums.pop()
            nums.appendleft(tmp)
            cnt += 1

print(cnt)
