import sys

# sys.stdin = open(
#     "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")

n = int(input())
dis = [[500] * (n+1) for _ in range(n + 1)]

for i in range(1, n+1):
    dis[i][i] = 0

while True:
    x, y = map(int, input().split())

    if x == -1 and y == -1:
        break

    dis[x][y] = 1
    dis[y][x] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(n+1):
    for j in range(n+1):
        if dis[i][j] == 500:
            dis[i][j] = 0

arr = []
for i in range(1, n+1):
    arr.append(max(dis[i]))

count = list(filter(lambda x: x == min(arr), arr))
print(min(arr), len(count))

for i in range(len(arr)):
    if arr[i] == min(arr):
        print(i+1, end=" ")
