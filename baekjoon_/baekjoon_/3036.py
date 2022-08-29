import sys
input = sys.stdin.readline

def gcd(a, b):
    while(b != 0):
        a, b = b, a % b
    return a

n = int(input())
r = list(map(int, input().split()))

for i in range(1, n):
    result = gcd(r[0], r[i])
    print('{0}/{1}'.format(r[0]//result, r[i]//result))
