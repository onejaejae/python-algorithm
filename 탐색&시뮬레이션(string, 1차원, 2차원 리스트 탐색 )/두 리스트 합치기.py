import sys
import os

sys.stdin = open(
    "c:\workspaces\python\탐색&시뮬레이션(string, 1차원, 2차원 리스트 탐색 )\input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

p1 = p2 = 0
c = []

while p1 < n and p2 < m:
    if arr[p1] < arr2[p2]:
        c.append(arr[p1])
        p1 += 1
    else:
        c.append(arr2[p2])
        p2 += 1

if p1 < n:
    c = c+arr[p1:]
else:
    c = c+arr2[p2:]
for x in c:
    print(x, end=" ")
