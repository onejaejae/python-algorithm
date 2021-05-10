import sys
import os

sys.stdin = open("c:\workspaces\python\DFS,BFS\input.txt", "rt")


def DFS(l, sum):
    global max
    if l == n+1:
        if sum > max:
            max = sum
    else:
        if l + days[l] <= n+1:
            DFS(l+days[l], sum+money[l])
        DFS(l+1, sum)


if __name__ == "__main__":
    n = int(input())

    days = list()
    money = list()
    max = -21600

    for _ in range(n):
        a, b = map(int, input().split())
        days.append(a)
        money.append(b)

    days.insert(0, 0)
    money.insert(0, 0)
    DFS(1, 0)
    print(max)
