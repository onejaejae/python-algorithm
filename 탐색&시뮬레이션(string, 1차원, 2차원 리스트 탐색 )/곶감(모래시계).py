import sys
import os

sys.stdin = open(
    "c:\workspaces\python\탐색&시뮬레이션(string, 1차원, 2차원 리스트 탐색 )\input.txt", "rt")


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            arr[h-1].append(arr[h-1].pop(0))
    else:
        for _ in range(k):
            arr[h-1].insert(0, arr[h-1].pop())

sum = 0
l = 0
r = n
for i in range(n):
    for j in range(l, r):
        sum += arr[i][j]
    if i < n//2:
        l += 1
        r -= 1
    else:
        l -= 1
        r += 1
print(sum)
