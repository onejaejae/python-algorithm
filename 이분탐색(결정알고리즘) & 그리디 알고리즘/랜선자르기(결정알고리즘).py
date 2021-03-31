import sys
import os

# sys.stdin = open(
#    "c:\workspaces\python\이분탐색(결정알고리즘) & 그리디 알고리즘\input.txt", "rt")

k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(tmp, largest)

lt = 1
rt = largest

while lt <= rt:
    count = 0
    mid = (lt + rt) // 2
    for x in Line:
        count += x//mid
    if count < n:
        rt = mid-1
    else:
        res = mid
        lt = mid+1

print(res)
