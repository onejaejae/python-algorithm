import sys
import os

sys.stdin = open(
    "c:\workspaces\python\완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초\input.txt", "rt")

n, m = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i][j], end=" ")
    print()
