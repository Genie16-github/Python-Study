# 쇠막대기
data = input()
data = data.replace('()', '*')
# print(data)
stack = []
total = 0

for i in data:
    if i == '(':
        stack.append(i)
    elif i == '*':
        total += len(stack)
    else:
        stack.pop()
        total += 1

print(total)