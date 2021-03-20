
import sys
import os

sys.stdin = open(
    "c:\workspaces\python\탐색&시뮬레이션(string, 1차원, 2차원 리스트 탐색 )\input.txt", "rt")

arr = [0] * 21
for i in range(len(arr)):
    arr[i] = i

# 0~20 배열 방법 #2
# arr = list(range(21))

for i in range(10):
    a, b = map(int, input().split())
    size = (b+1-a)//2

    for i in range(size):
        # tmp = arr[a+i]
        # arr[a+i] = arr[b-i]
        # arr[b-i] = tmp

        # python swap
        arr[a+i], arr[b-i] = arr[b-i], arr[a+i]

for x in arr:
    if x != 0:
        print(x, end=" ")
