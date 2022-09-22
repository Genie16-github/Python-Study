# [G5]도서관
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

left = []  # 음수
right = []  # 양수
for book in data:
    if book < 0:
        left.append(book)
    elif book > 0:
        right.append(book)

distance = []
left.sort()
for i in range(len(left) // m):
    distance.append(abs(left[m * i]))
if len(left) % m > 0:
    distance.append(abs(left[(len(left) // m) * m]))

right.sort(reverse=True)
for i in range(len(right) // m):
    distance.append(right[m * i])
if len(right) % m > 0:
    distance.append(right[(len(right) // m) * m])

distance.sort()
result = distance.pop()
result += 2 * sum(distance)
print(result)
