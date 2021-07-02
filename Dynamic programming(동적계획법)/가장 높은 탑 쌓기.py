import sys

# sys.stdin = open(
#    "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")

h = int(input())
bricks = []

for i in range(h):
    a, b, c = map(int, input().split())
    bricks.append((a, b, c))
bricks.sort(reverse=True)

dy = [0] * (h + 1)
dy[1] = bricks[0][1]
res = 0

for i in range(1, h):
    max = bricks[i][1]
    for j in range(i-1, -1, -1):
        if bricks[i][2] < bricks[j][2]:
            if max < dy[j+1] + bricks[i][1]:
                max = dy[j+1] + bricks[i][1]
    dy[i+1] = max
    if max > res:
        res = max
print(res)
