import sys
import os

sys.stdin = open(
    "c:\workspaces\python\이분탐색(결정알고리즘) & 그리디 알고리즘\input.txt", "rt")


n = int(input())
arr = list(map(int, input().split()))

lt = 0
rt = n-1
res = ""
tmp = []
last = 0
while lt <= rt:
    if arr[lt] > last:
        tmp.append((arr[lt], "L"))
    if arr[rt] > last:
        tmp.append((arr[rt], "R"))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res = res+tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == "L":
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)
