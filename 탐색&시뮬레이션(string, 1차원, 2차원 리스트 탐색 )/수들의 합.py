import sys
import os

sys.stdin = open(
    "c:\workspaces\python\탐색&시뮬레이션(string, 1차원, 2차원 리스트 탐색 )\input.txt", "rt")

n, m = map(int, input().split())

A = list(map(int, input().split()))

lt = 0
rt = 1
tot = A[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += A[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= A[lt]
        lt += 1
    else:
        tot -= A[lt]
        lt += 1

print(cnt)
