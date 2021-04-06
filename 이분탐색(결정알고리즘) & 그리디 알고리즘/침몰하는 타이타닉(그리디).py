import sys
import os

sys.stdin = open(
    "c:\workspaces\python\이분탐색(결정알고리즘) & 그리디 알고리즘\input.txt", "rt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
cnt = 0
while arr:
    if len(arr) == 1:
        cnt += 1
        break
    # -1은 list의 마지막 data
    if arr[0] + arr[-1] > m:
        # list의 마지막 data pop
        cnt += 1
        arr.pop()
    else:
        cnt += 1
        arr.pop()
        arr.pop(0)

print(cnt)
