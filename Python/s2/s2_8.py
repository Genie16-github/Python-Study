# 뒤집은 소수
import sys
input = sys.stdin.readline


def reverse(x):
    tmp = str(x)[::-1]
    num = int(tmp)

    return num


def isPrime(x):
    if x == 1:
        return False
    for k in range(2, x//2+1):
        if x % k == 0:
            return False
    else:
        return True


"""
def isPrime(x):
    ch = [0] * (x+1)
    for i in range(2, x+1):
        if ch[i] == 0:
            if i == x:
                print(i, end=' ')
            for j in range(i, x+1, i):
                ch[j] = 1
"""

N = int(input())
nums = list(map(int, input().split()))
for i in nums:
    res = reverse(i)
    if isPrime(res):
        print(res, end=' ')

"""
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
        
    return res
"""