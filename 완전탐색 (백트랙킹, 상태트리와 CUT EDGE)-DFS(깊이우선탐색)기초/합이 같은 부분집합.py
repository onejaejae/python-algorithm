import sys
import os

sys.stdin = open(
    "c:\workspaces\python\완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초\input.txt", "rt")


def DFS(l, sum):
    if l == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(l+1, sum + arr[l])
        DFS(l+1, sum)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    total = sum(arr)
    DFS(0, 0)
    print("NO")
