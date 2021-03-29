import sys
import os

sys.stdin = open(
    "c:\workspaces\python\탐색&시뮬레이션(string, 1차원, 2차원 리스트 탐색 )\input.txt", "rt")

arr = [list(map(int, input().split())) for _ in range(7)]
count = 0

for i in range(3):
    for j in range(7):
        tmp = arr[j][i:i+5]
        if tmp == tmp[::-1]:
            count += 1
        for k in range(2):
            if arr[i+k][j] != arr[i+5-k-1][j]:
                break
        else:
            count += 1
print(count)
