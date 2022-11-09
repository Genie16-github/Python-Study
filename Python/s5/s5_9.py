# 아나그램
tmp = input()
word1 = {x: 0 for x in list(set(tmp))}
tmp2 = input()
word2 = {x: 0 for x in list(set(tmp2))}

for x in tmp:
    word1[x] += 1

for x in tmp2:
    word2[x] += 1

if word1 == word2:
    print("YES")
else:
    print("NO")

"""
a = input()
b = input()
word = dict()

for x in a:
    word[x] = word.get(x, 0) + 1
for x in b:
    word[x] = word.get(x, 0) - 1

for x in a:
    if word.get(x) > 0
        print("NO")
        break
else:
    print("YES")
"""