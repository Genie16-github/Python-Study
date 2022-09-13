# [G4]단어 수학
import sys
input = sys.stdin.readline

alphabet = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0,
            'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0,
            'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

n = int(input())
data = [input().rstrip() for _ in range(n)]
num = []

for arr in data:
    for i in range(len(arr)):
        if arr[i] in alphabet:
            alphabet[arr[i]] += 10**(len(arr)-i-1)

for i in alphabet:
    if alphabet[i] > 0:
        num.append(alphabet[i])

num.sort(reverse=True)

sum = 0
m = 9
for i in range(len(num)):
    sum += num[i] * m
    m -= 1

print(sum)
