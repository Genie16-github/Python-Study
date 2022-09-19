# [S1]연산자 끼워넣기
import sys
input = sys.stdin.readline


def dfs(depth):
    global max_res, min_res, res
    if depth == n:
        max_res = max(res, max_res)
        min_res = min(res, min_res)
        return

    for i in range(4):
        tmp = res
        if op[i] > 0:
            if i == 0:
                res += num[depth]
            elif i == 1:
                res -= num[depth]
            elif i == 2:
                res *= num[depth]
            else:
                if res >= 0:
                    res //= num[depth]
                else:
                    res = (-res // num[depth]) * -1

            op[i] -= 1
            dfs(depth+1)
            res = tmp
            op[i] += 1


n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
max_res, min_res = -int(1e9), int(1e9)

res = num[0]

dfs(1)
print(max_res)
print(min_res)