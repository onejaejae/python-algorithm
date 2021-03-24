import sys
import os

sys.stdin = open(
    "c:\workspaces\python\탐색&시뮬레이션(string, 1차원, 2차원 리스트 탐색 )\input.txt", "rt")

n = int(input())

# for _ in은 변수없이 for문 돌리는것
arr = [list(map(int, input().split())) for _ in range(n)]

R_diagonal = 0
l_diagonal = 0
max = 0
max2 = 0

for i in range(n):
    R_diagonal += arr[i][i]
    l_diagonal += arr[i][n-1-i]

if R_diagonal > l_diagonal:
    max = R_diagonal
else:
    max = l_diagonal

for i in range(n):
    row = 0
    col = 0

    for j in range(n):
        row += arr[j][i]
        col += arr[i][j]
    if row > max2:
        max2 = row
    if col > max2:
        max2 = col

if max2 > max:
    print(max2)
else:
    print(max)
