# 자릿수의 합
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))


def digit_sum(x):
    res = 0
    for num in str(x):
        res += int(num)

    return res


max_num = -2147000000
for i in nums:
    tmp = digit_sum(i)
    if tmp > max_num:
        max_num = tmp
        ans = i

print(ans)


