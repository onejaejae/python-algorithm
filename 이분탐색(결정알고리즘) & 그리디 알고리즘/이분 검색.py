import sys
import os

# sys.stdin = open(
#     "c:\workspaces\python\이분탐색(결정알고리즘) & 그리디 알고리즘\input.txt", "rt")


n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)

start = 0
end = len(arr) - 1

while start <= end:
    mid = (start + end)//2

    if arr[mid] == m:
        print(mid+1)
        break
    elif arr[mid] < m:
        start = mid+1
    elif arr[mid] > m:
        end = mid-1
