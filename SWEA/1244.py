# [D3]최대 상금
def change(x):
    global res
    if x == 0:
        tmp = ''.join(list(map(str, nums)))
        if res < int(tmp):
            res = int(tmp)
        return

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            change(x-1)
            nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for tc in range(T):
    res = -2147000000
    N, M = map(int, input().split())
    nums = list(map(int, str(N)))

    if M > len(nums):
        M = len(nums)

    change(M)
    print('#%d %d' % (tc+1, res))
