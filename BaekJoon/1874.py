# [S2]스택 수열
import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

stack = []
num = 1
res = True
ans = ""

for i in range(n):
    su = nums[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            ans += "+\n"
        stack.pop()
        ans += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            res = False
            break
        else:
            ans += "-\n"

if res:
    print(ans)
