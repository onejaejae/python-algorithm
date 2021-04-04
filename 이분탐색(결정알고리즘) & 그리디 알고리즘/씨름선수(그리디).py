import sys
import os

# sys.stdin = open(
#    "c:\workspaces\python\이분탐색(결정알고리즘) & 그리디 알고리즘\input.txt", "rt")

n = int(input())
arr = []

for _ in range(n):
    s, m = map(int, input().split())
    arr.append((s, m))

arr.sort(reverse=True)

cnt = 1
for i in range(1, n):
    for j in range(i):
        if arr[i][1] < arr[j][1]:
            break
    else:
        cnt += 1

print(cnt)
