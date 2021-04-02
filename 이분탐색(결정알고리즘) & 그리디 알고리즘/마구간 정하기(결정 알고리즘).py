import sys
import os

# sys.stdin = open(
#     "c:\workspaces\python\이분탐색(결정알고리즘) & 그리디 알고리즘\input.txt", "rt")


def Count(mid):
    cnt = 1
    ep = arr[0]
    for i in range(1, n):
        if arr[i] - ep >= mid:
            ep = arr[i]
            cnt += 1
    return cnt


n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)
lt = 1
rt = max(arr)
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)
