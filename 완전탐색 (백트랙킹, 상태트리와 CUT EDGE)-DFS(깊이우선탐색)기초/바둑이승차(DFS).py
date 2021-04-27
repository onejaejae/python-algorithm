import sys
import os

# sys.stdin = open(
#    "c:\workspaces\python\완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초\input.txt", "rt")


def DFS(l, sum):
    global max
    if sum > c:
        return
    if l == n:
        if max < sum:
            max = sum
    else:
        DFS(l+1, sum+arr[l])
        DFS(l+1, sum)


if __name__ == "__main__":
    c, n = map(int, input().split())
    arr = []
    for _ in range(n):
        x = int(input())
        arr.append(x)
    max = 0
    DFS(0, 0)

print(max)
