import sys
input = sys.stdin.readline

n = int(input())
students = []

for _ in range(n):
    data = list(map(int, input().split(' ')))
    students.append(data)

students.sort(key=lambda student: student[2], reverse=True)

g = students[0]
s = students[1]

for i in range(2, len(students)):

    if g[0] == s[0] == students[i][0]:
        continue
    else:
        b = students[i]
        break

print(g[0], g[1])
print(s[0], s[1])
print(b[0], b[1])
