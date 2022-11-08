# 이분 검색
"""
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
print(nums.index(M)+1)
"""

# 이분 탐색을 이용해서 구현
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

lp = 0
rp = len(nums) - 1
while lp <= rp:
    md = (lp + rp) // 2
    if nums[md] == M:
        lp = rp = md
        break
    elif nums[md] > M:
        rp = md - 1
    else:  # 같은 경우
        lp = md + 1

print(lp+1)