# [S3]순열
import sys
from math import factorial
input = sys.stdin.readline

def permu(depth, string):
    global cnt
    if depth == len(a):
        cnt += 1
        if cnt == b:
            return string
    else:
        for k in a:
            if k not in string:
                res = permu(depth + 1, string + k)
                if res:
                    return res
    return


while True:
    try:
        a, b = input().split()
    except:
        break

    cnt = 0
    b = int(b)

    if factorial(len(a)) < b:
        print(a, b, '=', 'No permutation')
    else:
        print(a, b, '=', permu(0, ''))
