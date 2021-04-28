import sys
import os

sys.stdin = open(
    "c:\workspaces\python\완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초\input.txt", "rt")


def DFS(l):
    global cnt
    if l == m:
        for x in res:
            print(x, end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            res[l] = i
            DFS(l+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*m
    cnt = 0
    DFS(0)
    print(cnt)
