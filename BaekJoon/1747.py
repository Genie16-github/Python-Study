# [S1]소수&팰린드롬
import math
n = int(input())
a = [0] * 10000001

for i in range(2, len(a)):
    a[i] = i

for i in range(2, int(math.sqrt(len(a)) + 1)):
    if a[i] == 0:
        continue
    for j in range(i + i, len(a), i):
        a[j] = 0


def isPalindrome(target):
    tmp = list(str(target))
    s = 0
    e = len(tmp) - 1
    while s < e:
        if tmp[s] != tmp[e]:
            return False
        s += 1
        e -= 1
    return True

i = n
while True:
    if a[i] != 0:
        res = a[i]
        if isPalindrome(res):
            print(res)
            break
    i += 1