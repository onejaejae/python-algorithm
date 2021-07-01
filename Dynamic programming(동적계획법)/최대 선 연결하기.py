import sys

# sys.stdin = open(
# "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

res = 0
dy = [0] * n
dy[0] = 1

for i in range(1, n):
    max = 1
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i]:
            if max < dy[j] + 1:
                max = dy[j] + 1
    dy[i] = max
    if res < max:
        res = max
print(res)
