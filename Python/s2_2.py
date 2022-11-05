# K번째 수
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, s, e, k = map(int, input().split())  # N(5<=N<=500)
    nums = list(map(int, input().split()))  # N개의 숫자

    # s번째부터 e번째 까지의 수를 오름 차순 정렬
    # K번째 수 출력
    arr = sorted(nums[s-1:e])
    print("#{0} {1}".format(i+1, arr[k-1]))
