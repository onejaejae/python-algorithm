import sys
import os

sys.stdin = open(
    "c:\workspaces\python\완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초\input.txt", "rt")


def DFS(l, sum):
    if l == n and sum == f:
        for x in p:
            print(x, end=" ")
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[l] = i
                DFS(l+1, sum+(p[l] * b[l]))
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0]*n
    b = [1]*n
    ch = [0]*(n+1)
    for i in range(1, n):
        b[i] = b[i-1]*(n-1)//i
    DFS(0, 0)
