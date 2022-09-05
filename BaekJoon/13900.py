# [S4]순서쌍의 곱의 합
def combi(depth, start):
    global sum
    if depth == 2:
        sum += isSelected[0] * isSelected[1]
        return

    for i in range(start, n):
        isSelected[depth] = number[i]
        combi(depth+1, i+1)


n = int(input())
number = list(map(int, input().split()))
isSelected = [0] * 2   # nC2
sum = 0

combi(0, 0)

print(sum)