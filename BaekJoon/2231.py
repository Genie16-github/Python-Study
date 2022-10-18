# [B2] 분해합
n = int(input())
print(min([n for n in range(max(n-54, 1), n) if n == n + sum(map(int, str(n)))], default=0))