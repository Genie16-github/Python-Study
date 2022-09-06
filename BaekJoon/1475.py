# [S5]방 번호
data = input()
num = [0] * 10

for i in data:
    if i == '6' or i == '9':
        if num[6] == num[9]: 
            num[6] += 1
        else:
            num[9] += 1
    else:
        num[int(i)] += 1

print(max(num))
