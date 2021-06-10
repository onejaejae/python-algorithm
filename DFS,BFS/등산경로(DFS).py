import sys
import os

sys.stdin = open("c:\workspaces\python\DFS,BFS\input.txt", "rt")

# 상하좌우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt, n

    if x == n-1 and y == n-1:
        cnt += 1
    else:
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0 <= xx < n and 0 <= yy < n and board[x][y] < board[xx][yy] and dis[xx][yy] == 0:
                dis[xx][yy] = 1
                DFS(xx, yy)
                dis[xx][yy] = 0


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dis = [[0]*n for _ in range(n)]

    dis[0][0] = 1
    cnt = 0
    DFS(0, 0)
    print(cnt)
