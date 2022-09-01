import sys
input = sys.stdin.readline

n = int(input())
t_num = sorted(list(map(int, input().split())))

for i in range(1, n+1):
    if t_num[i-1] == i:
        continue
    else:
        print(i)
        sys.exit()

print(n+1)
