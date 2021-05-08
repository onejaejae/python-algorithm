import sys
import os

sys.stdin = open(
    "c:\workspaces\python\완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초\input.txt", "rt")


def DFS(l, sum):
    if sum > m:
        return
    if sum == m:
        print(l)
        sys.exit(0)
    else:
        for i in range(n):
            DFS(l+1, sum + arr[i])


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    res = -2200
    arr.sort(reverse=True)

    DFS(0, 0)
