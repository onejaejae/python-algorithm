from os import rename
import sys

sys.stdin = open(
    "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")


def dfs(x, y):
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if y == 0:
            return dfs(x-1, y)+arr[x][y]
        elif x == 0:
            return dfs(x, y-1) + arr[x][y]
        else:
            return min(dfs(x-1, y), dfs(x, y-1)) + arr[x][y]


if __name__ == "__name__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]

    print(dfs(n-1, n-1))
