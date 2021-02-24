import sys
import os

sys.stdin = open("c:\workspaces\python\코드 구현력 기르기\input.txt", "rt")

T = int(input())
for t in range(T):
    i = 1
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = arr[s-1:e]
    arr.sort()

    print("#%d %d" % (t+1, arr[k-1]))
