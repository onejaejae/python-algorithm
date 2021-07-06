import sys

sys.stdin = open(
    "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
dy = [1000] * (m+1)
dy[0] = 0

for x in arr:
    for i in range(x, m+1):
        dy[i] = min(dy[i], dy[i-x]+1)

print(dy[m])
