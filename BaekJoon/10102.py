n = int(input())
arr = input()

cnt = 0

for i in range(n):
    if arr[i] == 'A':
        cnt += 1

if cnt > n/2:
    print('A')
elif cnt < n/2:
    print('B')
else:
    print('Tie')
