import sys
import os

# sys.stdin = open(
#    "c:\workspaces\python\완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초\input.txt", "rt")


def DFS(x):
    if x == 0:
        return
    DFS(x//2)
    print(x % 2, end="")


n = int(input())
DFS(n)
