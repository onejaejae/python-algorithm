import sys
import os

sys.stdin = open(
    "c:\workspaces\python\탐색&시뮬레이션(string, 1차원, 2차원 리스트 탐색 )\input.txt"
)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.insert(0, [0] * n)
arr.append([0]*n)

for i in range(n+2):
    arr[i].insert(0, 0)
    arr[i].append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        # all 함수는 모두가 참일때 true
        if all(arr[i][j] > arr[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
