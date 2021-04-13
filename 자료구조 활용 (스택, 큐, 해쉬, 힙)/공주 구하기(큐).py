import sys
import os
from collections import deque

sys.stdin = open("c:\workspaces\python\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

n, k = map(int, input().split())
dq = list(range(1, n+1))

# dq list를 deque로 만들기
dq = deque(dq)

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        break
