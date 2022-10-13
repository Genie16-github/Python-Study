# [S5]달팽이는 올라가고 싶다
import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
me = (v-a) // (a-b) + 1
print(me if (v-a) % (a-b) == 0 else me+1)