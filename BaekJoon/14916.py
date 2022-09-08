# [S5]거스름돈
n = int(input())
change = n % 5

if n == 1 or n == 3:
    result = -1
elif change % 2 == 0:
    result = n // 5 + change // 2
else:
    result = ((n // 5) - 1) + ((change + 5) // 2)

print(result)
