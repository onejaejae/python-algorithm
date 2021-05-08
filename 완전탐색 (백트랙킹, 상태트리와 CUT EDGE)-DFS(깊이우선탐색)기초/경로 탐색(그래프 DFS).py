import sys
import os

# sys.stdin = open(
#    "c:\workspaces\python\완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초\input.txt", "rt")


def DFS(l):
    global cnt
    if l == n:
        cnt += 1
    else:
        for i in range(1, n+1):
            if arr[l][i] == 1 and ch[i] == 0:
                ch[i] = 1
                DFS(i)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    ch = [0] * (n+1)
    ch[1] = 1
    cnt = 0

    for _ in range(m):
        a, b = map(int, input().split())
        arr[a][b] = 1

    DFS(1)
    print(cnt)
