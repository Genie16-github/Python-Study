# 크로아티아 알파벳
import sys
input = sys.stdin.readline

alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
data = input()
for i in alphabet:
    data = data.replace(i, '*')

print(len(data.strip()))
