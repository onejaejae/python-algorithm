import sys
import os

sys.stdin = open("c:\workspaces\python\DFS,BFS\input.txt", "rt")


def DFS(l, sum, time):
    global res
    if l == n:
        if time > m:
            return
        else:
            if res < sum:
                res = sum
    else:
        DFS(l+1, sum+pv[l], time+pt[l])
        DFS(l+1, sum, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -2147000
    DFS(0, 0, 0)
    print(res)
