import sys
import os

#sys.stdin = open("c:\workspaces\python\DFS,BFS\input.txt", "rt")


def DFS(l):
    global result
    if l == n:
        cha = max(money) - min(money)
        if result > cha:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                result = cha
    else:
        for i in range(3):
            money[i] += m[l]
            DFS(l+1)
            money[i] -= m[l]


if __name__ == "__main__":
    n = int(input())
    m = list()
    money = [0] * 3

    for _ in range(n):
        x = int(input())
        m.append(x)

    result = 100000
    DFS(0)
    print(result)
