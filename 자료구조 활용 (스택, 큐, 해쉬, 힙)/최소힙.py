import sys
import os
import heapq

#sys.stdin = open("c:\workspaces\python\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

heap = []
while True:
    n = int(input())

    if n == -1:
        break

    if n == 0:
        if len(heap) == 0:
            print(-1)
        else:
            result = heapq.heappop(heap)
            print(result)
    else:
        heapq.heappush(heap, n)
