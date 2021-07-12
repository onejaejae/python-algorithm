import sys

# sys.stdin = open(
#    "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")

# 해당문제는해당시간이 걸리면 푸는 걸로 간주한다, 한 유형당 한개만 풀 수 있습니다. => 2차원 배열로 풀이

n, m = map(int, input().split())
dy = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    x, y = map(int, input().split())
    for j in range(0, m+1):
        dy[i][j] = dy[i-1][j]
        if j >= y:
            dy[i][j] = max(dy[i][j], x + dy[i-1][j-y])

print(dy[n][m])
