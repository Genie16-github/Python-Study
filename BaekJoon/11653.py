# [B1]소인수분해
n = int(input())
d = 2
while d*d <= n:
    if n % d == 0:
        print(d)
        n //= d
    else:
        d += 2 if d > 2 else 1
if n > 1:
    print(n)