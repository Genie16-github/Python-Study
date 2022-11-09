# 후위(postfix) 연산(스택)
exp = input()
stack = []
res = 0

for x in exp:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            stack.append(stack.pop() + stack.pop())
        elif x == '-':
            stack.append(-(stack.pop()) + stack.pop())
        elif x == '*':
            stack.append(stack.pop() * stack.pop())
        elif x == '/':
            stack.append(1 / stack.pop() * stack.pop())

while stack:
    res += stack.pop()

print(res)