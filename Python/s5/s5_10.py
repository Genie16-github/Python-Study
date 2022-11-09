# 아나그램(리스트 해쉬)
a = input()
b = input()
str1 = [0] * 52
str2 = [0] * 52

for x in a:
    if x.isupper():  # 대문자인지 알려줌. 소문자는 islower()
        str1[ord(x)-65] += 1
    else:
        str1[ord(x)-71] += 1

for x in b:
    if x.isupper():  # 대문자인지 알려줌. 소문자는 islower()
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1

if str1 == str2:
    print("YES")
else:
    print("NO")