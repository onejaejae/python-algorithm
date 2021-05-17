import sys
import os
from collections import deque

sys.stdin = open("c:\workspaces\python\DFS,BFS\input.txt", "rt")

max = 10000
ch = [0]*10000
dis = [0]*10000
n, m = map(int, input().split())
ch[n] = 1
dq = deque()
dq.append(n)
while dq:
    now = dq.popleft()
    if now == m:
        print(dis[now])
        break
    for next in (now-1, now+1, now+5):
        if 1 < next <= max:
            if ch[next] == 0:
                dq.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1
