import sys
import os

sys.stdin = open(
    "c:\workspaces\python\이분탐색(결정알고리즘) & 그리디 알고리즘\input.txt", "rt")

n = int(input())
arr = []

for _ in range(n):
    s, m = map(int, input().split())
    arr.append((s, m))

arr.sort(reverse=True)

cnt = 0
largest = 0

for x, y in arr:
    if y > largest:
        largest = y
        cnt += 1

print(cnt)
