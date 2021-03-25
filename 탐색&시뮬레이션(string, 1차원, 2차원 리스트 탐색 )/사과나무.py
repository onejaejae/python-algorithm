import sys
import os

sys.stdin = open(
    "c:\workspaces\python\탐색&시뮬레이션(string, 1차원, 2차원 리스트 탐색 )\input.txt", "rt")


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
s = e = n//2

for i in range(n):
    for j in range(s, e+1):
        res += arr[i][j]

    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)
