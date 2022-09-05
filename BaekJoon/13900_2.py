# [S4]순서쌍의 곱의 합
n = int(input())
nums = list(map(int, input().split()))

sum_nums = sum(nums)
res = 0

for i in nums:
    sum_nums -= i
    res += sum_nums * i

print(res)
