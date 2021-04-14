import sys
import os
from collections import deque

sys.stdin = open("c:\workspaces\python\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

n, m = map(int, input().split())
dq = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
dq = deque(dq)
cnt = 0

while dq:
    cur = dq.popleft()
    if any(cur[1] < x[1] for x in dq):
        dq.append(cur)
    else:
        cnt += 1
        if m == cur[0]:
            print(cnt)
            break
