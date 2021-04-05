import sys
import os

# sys.stdin = open(
#    "c:\workspaces\python\이분탐색(결정알고리즘) & 그리디 알고리즘\input.txt", "rt")


l = int(input())
arr = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    largest = arr.index(max(arr))
    lowest = arr.index(min(arr))
    arr[largest] -= 1
    arr[lowest] += 1

print(max(arr) - min(arr))
