import sys

# sys.stdin = open(
#   "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))
dy = [0] * (n)
dy[0] = 1

for i in range(1, n):
    max = 1
    for j in range(0, i):
        if arr[i] > arr[j]:
            if max < dy[j] + 1:
                max = dy[j] + 1
    dy[i] = max


max = dy[0]
for i in range(1, n):
    if max < dy[i]:
        max = dy[i]

print(max)
