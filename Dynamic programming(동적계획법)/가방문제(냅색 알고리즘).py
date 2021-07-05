import sys

sys.stdin = open(
    "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")

n, limit = map(int, input().split())
dy = [0] * (limit+1)

for i in range(n):
    w, v = map(int, input().split())

    for j in range(w, limit+1):
        dy[j] = max(dy[j], dy[j-w] + v)

print(dy[limit])
