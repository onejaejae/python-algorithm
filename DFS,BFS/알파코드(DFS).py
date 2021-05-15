import sys
import os

sys.stdin = open("c:\workspaces\python\DFS,BFS\input.txt", "rt")


def DFS(l, p):
    global cnt
    if l == len(code) - 1:
        cnt += 1
        for j in range(p):
            print(chr(res[j]+64), end="")
        print()
    else:
        for i in range(1, 27):
            if code[l] == i:
                res[p] = i
                DFS(l+1, p+1)
            elif i >= 10 and code[l] == i//10 and code[l+1] == i % 10:
                res[p] = i
                DFS(l+2, p+1)


if __name__ == "__main__":
    code = list(map(int, input()))
    code.insert(len(code), -1)
    res = [0] * (len(code)+3)
    cnt = 0
    DFS(0, 0)
    print(cnt)
