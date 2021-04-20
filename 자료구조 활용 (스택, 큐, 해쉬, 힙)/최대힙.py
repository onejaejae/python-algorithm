import sys
import os
import heapq

#sys.stdin = open("c:\workspaces\python\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

maxHeap = []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(maxHeap) == 0:
            print(-1)
        else:
            print(heapq.heappop(maxHeap)[1])
    else:
        heapq.heappush(maxHeap, (-n, n))
