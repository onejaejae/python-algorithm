import sys
import os
from collections import deque

#sys.stdin = open("c:\workspaces\python\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

need = input()
n = int(input())

for i in range(n):
    flag = True
    dq = deque(need)
    arr = list(input())

    for j in range(len(arr)):
        if any(arr[j] == x for x in dq):

            if arr[j] != dq.popleft():
                flag = False
                break
    if(flag and len(dq) == 0):
        print("#%d YES" % (i+1))
    else:
        print("#%d NO" % (i+1))
