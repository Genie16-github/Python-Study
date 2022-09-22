# [G5]0 만들기
import sys
input = sys.stdin.readline


def dfs(total, sign, num, now, num_str):
    global n
    if now == n:
        total += (num * sign)
        if total == 0:
            print(num_str)
        return
    dfs(total, sign, num * 10 + (now + 1), now + 1, num_str + " " + str(now + 1))
    dfs(total + (sign * num), 1, now + 1, now + 1, num_str + "+" + str(now + 1))
    dfs(total + (sign * num), -1, now + 1, now + 1, num_str + "-" + str(now + 1))


t = int(input())
for i in range(t):
    n = int(input())
    numberStr = "1"
    dfs(0, 1, 1, 1, numberStr)
    print()
