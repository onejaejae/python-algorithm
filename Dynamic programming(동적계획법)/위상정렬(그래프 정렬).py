import sys
from collections import deque

# sys.stdin = open(
#    "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")

deq = deque()
n, m = map(int, input().split())

order = [[0] * (n+1) for _ in range(n+1)]
degree = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    order[x][y] = 1
    degree[y] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        deq.append(i)


while deq:
    tmp = deq.popleft()
    print(tmp, end=" ")

    for j in range(1, n+1):
        if order[tmp][j] == 1:
            degree[j] -= 1
            if degree[j] == 0:
                deq.append(j)
