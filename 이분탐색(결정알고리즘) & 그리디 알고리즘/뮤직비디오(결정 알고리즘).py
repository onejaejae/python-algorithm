import sys
import os

sys.stdin = open(
    "c:\workspaces\python\이분탐색(결정알고리즘) & 그리디 알고리즘\input.txt", "rt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))


def Count(mid):
    cnt = 1
    sum = 0
    for x in arr:
        if sum+x > mid:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


lt = 1
rt = sum(arr)
res = 0
largest = max(arr)
while lt <= rt:
    mid = (lt+rt)//2
    if largest <= mid and Count(mid) <= m:
        res = mid
        rt = mid-1
    else:
        lt = mid + 1
print(res)
