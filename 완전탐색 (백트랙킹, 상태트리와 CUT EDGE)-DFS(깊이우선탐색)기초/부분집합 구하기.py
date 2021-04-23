import sys
import os

sys.stdin = open(
    "c:\workspaces\python\완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초\input.txt", "rt")


def DFS(v):
    if v == n+1:
        for i, value in enumerate(ch):
            if value == 1:
                print(i, end=" ")
        print()
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)


n = int(input())
ch = [0]*(n+1)
DFS(1)
