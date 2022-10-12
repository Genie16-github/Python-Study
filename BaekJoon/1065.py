# [S4]한수
import sys
input = sys.stdin.readline


def func_hs(x):
    cnt = 0
    for i in range(1, x+1):
        if i > 99:
            num_list = list(map(int, str(i)))
            if num_list[2]-num_list[1] == num_list[1] - num_list[0]:
                cnt += 1
        else:
            cnt += 1

    return cnt


n = int(input())
print(func_hs(n))
