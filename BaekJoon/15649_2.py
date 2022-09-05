# [S3]N과 M(1)
from itertools import permutations

n, m = map(int, input().split())
number = map(str, range(1, n+1))
print('\n'.join(list(map(' '.join, permutations(number, m)))))