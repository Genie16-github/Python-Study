# [S5]백대열
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

n, m = map(int, input().split(':'))
g = gcd(max(n, m), min(n, m))
result=f'{n//g}:{m//g}'
print(result)