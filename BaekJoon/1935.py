# [S3]후위 표기식2
N = int(input())
exp = input()
nums = [int(input()) for _ in range(N)]
stack = []
res = 0

for x in exp:
    if x.isalpha():
        stack.append(nums[ord(x)-ord('A')])
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

print('%.2f' % res)

