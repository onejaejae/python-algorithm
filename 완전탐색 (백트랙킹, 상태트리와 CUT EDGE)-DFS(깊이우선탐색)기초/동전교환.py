import sys
import os

# sys.stdin = open(
#    "c:\workspaces\python\완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초\input.txt", "rt")


def DFS(l):
    global m, cnt

    if m % arr[l] == 0:
        cnt += m // arr[l]
        return
    else:
        if m // arr[l] < 1:
            DFS(l+1)
        else:
            cnt += m//arr[l]

            m = m % arr[l]
            DFS(l+1)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    arr.sort(reverse=True)

    DFS(0)
    print(cnt)
