import sys
import os

#sys.stdin = open("c:\workspaces\python\DFS,BFS\input.txt", "rt")


def DFS(l, sum):
    global p, cnt

    if l == k:

        if sum == t:
            cnt += 1
    else:
        for i in range(s[l]+1):
            if sum + (m[l] * i) > t:
                break
            DFS(l+1, sum + (m[l] * i))


if __name__ == "__main__":
    t = int(input())
    k = int(input())
    m = list()
    s = list()
    cnt = 0

    for _ in range(k):
        p, n = map(int, input().split())
        m.append(p)
        s.append(n)

    DFS(0, 0)
    print(cnt)
