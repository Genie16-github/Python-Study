n, m, v = map(int, input().split())
v = v - 1  # 3번째 노드면 인덱스는 2
c = list(map(int, input().split()))
answer = list()
len_cycle = n - v

for i in range(0, m):
    k = int(input())
    if k < n:
        answer.append(c[k])
    else:
        tmp = (k-v) % len_cycle
        answer.append(c[v+tmp])

for i in answer:
    print(i)
