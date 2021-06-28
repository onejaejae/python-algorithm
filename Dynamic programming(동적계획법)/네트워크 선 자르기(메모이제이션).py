import sys

sys.stdin = open(
    "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")


def DFS(len):
    if dy[len] > 0:
        return dy[len]
    if len == 2 or len == 1:
        return len
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]


if __name__ == "__main__":
    n = int(input())
    dy = [0]*(n+1)

    print(DFS(n))
