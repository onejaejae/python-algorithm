import sys
import os


sys.stdin = open(

    "c:\workspaces\python\완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초\input.txt", "rt")


def DFS(l, s, sum):
    global cnt
    if l == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(l+1, i+1, sum + arr[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
