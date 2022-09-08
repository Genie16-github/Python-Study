# [S5]과일노리
n = int(input())
bot = []
time = 0

for i in range(n):
    a, b = map(int, input().split())
    bot.append([a, b])
time += bot[0][1]

i=1
while i < n:
    time += 1
    if time % (bot[i][0] + bot[i][1]) >= bot[i][1]:
        i += 1
    else:
        time += (bot[i][1] - time % (bot[i][0] + bot[i][1]) - 1)
time += 1
print(time)
