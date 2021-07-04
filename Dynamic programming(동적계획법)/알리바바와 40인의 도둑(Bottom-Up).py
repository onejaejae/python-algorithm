from os import rename
import sys

sys.stdin = open(
    "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
score = [[0]*n for _ in range(n)]
score[0][0] = board[0][0]

for i in range(1, n):
    score[0][i] = score[0][i-1] + board[0][i]
    score[i][0] = score[i-1][0] + board[i][0]

for i in range(1, n):
    for j in range(1, n):
        score[i][j] = min(score[i-1][j], score[i][j-1]) + board[i][j]

print(score[n-1][n-1])
